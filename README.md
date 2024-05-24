# Development of a Speech Annotation Tool Using the Example of Kazym Northern Khanty Language

Despite significant advancements in speech processing technologies, including automatic speech recognition, diarization, and spoken language identification (e.g., Park et al., 2022; Li, 2022), many low-resource languages remain underrepresented in this domain. In this project, we develop several speech processing tools for Kazym Khanty, a low-resource Finno-Ugric language spoken by approximately 9,500 people in western Siberia, according to the 2010 census (Russian Federal State Statistics Service, 2010).

## Project Goals

We outline several goals for our project:

1. **Fine-Tuning a Diarization Model**
   - We aim to fine-tune a Pyannote.audio diarization model on our data. A speaker diarization system tailored for a low-resource language like Khanty can greatly assist researchers by making the transcription process of elicitation sessions with Khanty speakers more efficient.

2. **Creating an ASR Model for Khanty Language**
   - We intend to fine-tune a multilingual Whisper model on our data to develop an automatic speech recognition (ASR) system for the Khanty language. An ASR system specifically developed for Khanty can significantly aid researchers in collecting data for text corpora and transcribing elicitation sessions and monologues by Khanty speakers. Even with moderate quality and a high word error rate (WER), an ASR model can enhance the efficiency of the transcription process.

3. **Developing a Language Identification Model**
   - We plan to initiate efforts to create a language identification model capable of distinguishing between Khanty and Russian languages by testing the performance of the SpeechBrain language identification model. When used in conjunction with the diarization model, this language identification model could potentially make the transcription process more efficient by isolating segments of Khanty speech, allowing researchers to concentrate on these specific segments.

## Data Collection

To develop the diarization and ASR tools, we compiled two novel datasets of audio recordings with Khanty speakers conducted between 2018 and 2024:

- **Diarization Dataset**
  - This dataset includes 26 audio recordings, totaling 1,273 minutes, annotated for speaker turns, start and end times of speech fragments, and the language spoken. These recordings feature one-on-one elicitation sessions with native speakers, conducted in both Russian and Khanty.

- **ASR Dataset**
  - This dataset consists of 5 hours of annotated speech data, with annotations provided by participants of expeditions to Kazym village or sourced from the online version of the newspaper "Хӑнты ясӑң" (Khanty Language). The content includes monologues, dialogues, tales, stories, and news about the politics and life of the Ob-Ugric people.

## Results

We achieved the following results:

1. **Diarization Model Improvement**
   - Improved the performance of the diarization model from 38.9% to 26.3% DER.

2. **ASR Model Performance**
   - Achieved a 44.57% WER with our ASR model. Despite the high WER, we received positive feedback from the Kazym Khanty research community.

3. **Language Identification Model Testing**
   - Tested the SLID model on our data and achieved only 51% accuracy for distinguishing between Khanty and Russian speech fragments. We conclude that additional fine-tuning on a different dataset is needed to achieve competitive results.

## Repository Structure

In this repository, we store the code for our project and some of the data. This repository is structured as follows:

