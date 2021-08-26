# Voice Interface Demo (Python)

Demonstrates voice interface capabilities. Uses the "SpeechRecognition" Python package to convert speech to text.

## Prerequisites

The "SpeechRecognition" package depends on the "pyaudio" Python package, which in turn depends on the lower-level "portaudio" library. To install "portaudio":

  + On a Mac, use homebrew (`brew install portaudio`).
  + On Windows, use pipwin within an active virtual environment (see installation steps below).


## Installation

Fork this repo under your own control, then clone your copy onto your local computer and navigate there from the command-line:

```sh
cd voice-interface-demo-py/
```

## Setup

Create and activate a virtual environment:

```sh
conda create -n voice-env python=3.8
conda activate voice-env
```

Windows only:

```sh
pip install pipwin
pipwin install pyaudio
```

Install package dependencies:

```sh
pip install -r requirements.txt
```



## Usage

Recognize speech and respond with print statements:

```sh
python app/demo.py
```
