# Ugandan Language Translation & Transcription Project

Hey there! 👋 This is a Sunbird AI internship assessment project working with Ugandan languages using the Sunbird AI API. It's got two main features:

1. **Text Translation**: Translate between English and 5 local Ugandan languages
2. **Audio Transcription**: Turn audio files into text in any of these languages

## What Languages Can I Use?

Here are the languages I've got working:
- English (eng)
- Luganda (lug)
- Runyankole (nyn)
- Ateso (teo)
- Lugbara (lgg)
- Acholi (ach)

## Getting Started

### What You'll Need
- Python 3.x (I used Python 3.8)
- pip (for installing packages)
- A Sunbird AI API token (you'll get this from Sunbird)

### Setting Up
1. First, clone this repo:
```bash
git clone <repository>
cd <repository-directory>
```

2. Set up your Python environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install what you need:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project folder and add your API token:
```
AUTH_TOKEN=your_api_token_here
```

## How to Use It

### For Translation
Just run:
```bash
python translate.py
```
It'll ask you:
- What language you're translating from
- What language you want to translate to
- The text you want to translate

### For Audio Transcription
Run:
```bash
python transcribe.py
```
You'll need to:
- Choose the language of your audio file
- Point to where your audio file is (must be less than 5 minutes)

## What's in the Project?

Here's what I've built:
- `translate.py`: The translation script
- `transcribe.py`: The audio transcription script
- `tests/`: My tests

## Running Tests

To check if everything's working:
```bash
pytest
```


## Thanks!

Big thanks to:
- Sunbird AI for their awesome API


