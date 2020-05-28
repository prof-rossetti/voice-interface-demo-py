# Voice Interface Capabilities Demo (Python)

Demonstrates voice interface capabilities. Uses the `SpeechRecognition` Python package to convert speech to text.

## Prerequisites

  + Anaconda, Python 3.7
  + [portaudio](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/speech_recognition.md#prerequisites)

## Installation

Fork this repo under your own control, then clone your copy onto your local computer and navigate there from the command-line:

```sh
cd voice-interface-py/
```

## Setup

```sh
conda create -n interface-capabilities-env python=3.7
conda activate interface-capabilities-env
```

```sh
pip install -r requirements.txt
```

## Usage

Recognize speech and respond with print statements:

```sh
python interfaces/voice.py
```

Recognize speech, and respond with voice output (Mac only):

```sh
python interfaces/voice_mac.py
```
