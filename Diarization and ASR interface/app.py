import gradio as gr
from transformers import pipeline
from pyannote.audio import Audio, Model, Pipeline
from pyannote.audio.pipelines import SpeakerDiarization
from pympi import Eaf

# Load the finetuned model and pipeline
finetuned_model = Model.from_pretrained('/Users/polyakarpova/Desktop/diarapp/epoch=4.ckpt', strict=False)
pretrained_pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", use_auth_token= HUGGING_TOKEN )

finetuned_pipeline = SpeakerDiarization(
    segmentation=finetuned_model,
    embedding=pretrained_pipeline.embedding,
    embedding_exclude_overlap=pretrained_pipeline.embedding_exclude_overlap,
    clustering=pretrained_pipeline.klustering,
)

finetuned_pipeline.instantiate({
    "segmentation": {
        "threshold": 0.7059725947191872,
        "min_duration_off": 0.0,
    },
    "clustering": {
        "method": "centroid",
        "min_cluster_size": 15,
        "threshold": 0.593157817904834,
    },
})

# Load ASR model
asr_pipeline = pipeline("automatic-speech-recognition", model="numblilbug/khanty_whisper_asr")

# Function to perform diarization and transform the output into an eaf file
def diarization_and_convert_to_eaf(audio_file):
    # Load audio
    io = Audio(mono='downmix', sample_rate=16000)
    waveform, sample_rate = io(audio_file)

    # Perform diarization
    diarization = finetuned_pipeline({"waveform": waveform, "sample_rate": sample_rate})

    # Convert diarization result to EAF
    rttm_file = "output.rttm"
    with open(rttm_file, 'w') as file_object:
        diarization.write_rttm(file_object)

    eaf_file = "output.eaf"
    rttm_to_eaf(rttm_file, eaf_file)

    return eaf_file

# Function to perform ASR and save result to a text file
def asr_and_convert_to_txt(audio_file):
    result = asr_pipeline(audio_file)
    text_file = "output.txt"
    with open(text_file, 'w') as file_object:
        file_object.write(result['text'])
    return text_file

# Function to transform rttm file to eaf file
def rttm_to_eaf(rttm_file, eaf_file):
    with open(rttm_file, 'r') as f:
        lines = f.readlines()

    eaf = Eaf()  # Initialize Eaf object
    tier_names = set()

    for line in lines:
        components = line.strip().split()
        tier_names.add(components[7])

    for tier_name in tier_names:
        eaf.add_tier(tier_name)

    for line in lines:
        components = line.strip().split()
        start_time = int(float(components[3]) * 1000)
        end_time = int((float(components[3]) + float(components[4])) * 1000)
        tier_name = components[7]
        eaf.add_annotation(tier_name, start_time, end_time, "")

    eaf.to_file(eaf_file)

# Gradio interface
def process_audio(audio_file, task):
    if task == "Diarization":
        return diarization_and_convert_to_eaf(audio_file)
    elif task == "ASR":
        return asr_and_convert_to_txt(audio_file)

gr.Interface(
    fn=process_audio,
    inputs=[gr.Audio(type="filepath"), gr.Radio(["Diarization", "ASR"], label="Task")],
    outputs="file",
    title="Speaker Diarization and ASR for Kazym Khanty Language",
    description="Upload an audio file to perform speaker diarization or ASR. Get the result in EAF or TXT format respectively.",
    allow_flagging=False
).launch(share=True)
