# Voice Interface Demo (Python)

Demonstrates voice interface capabilities. Uses the `SpeechRecognition` Python package to convert speech to text.

## Prerequisites

  + Anaconda, Python 3.8
  + [portaudio](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/speech_recognition.md#prerequisites)

## Installation

Fork this repo under your own control, then clone your copy onto your local computer and navigate there from the command-line:

```sh
cd voice-interface-demo-py/
```

## Setup

```sh
conda create -n interface-capabilities-env python=3.8
conda activate interface-capabilities-env
```

```sh
pip install -r requirements.txt
```

## Usage

Recognize speech and respond with print statements:

```sh
python app/demo.py
```
