#!/usr/bin/env python3
"""
A simple audio transcription script using Sunbird AI API.
This script helps transcribe audio files in English and 5 local Ugandan languages.
"""

import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# API configuration
API_URL = "https://api.sunbird.ai/tasks/stt"
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

# Language codes mapping
LANGUAGE_CODES = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Acholi": "ach",
    "Ateso": "teo",
    "Lugbara": "lgg"
}

def get_language_input(prompt):
    """
    Get and validate language input from user.
    Keeps asking until a valid language is entered.
    """
    valid_languages = list(LANGUAGE_CODES.keys())
    while True:
        language = input(prompt).strip().capitalize()
        if language in valid_languages:
            return language
        print(f"Oops! Please choose one of: {', '.join(valid_languages)}")

def get_audio_file_path():
    """
    Get and validate audio file path from user.
    Checks if file exists and is less than 5 minutes.
    """
    while True:
        file_path = input("\nPlease provide path to the audio file (Audio length less than 5 minutes): ").strip()
        
        # Check if file exists
        if not os.path.exists(file_path):
            print("Error: File does not exist. Please try again.")
            continue
            
        # Check if file is an audio file
        if not file_path.lower().endswith(('.mp3', '.wav', '.ogg', '.m4a')):
            print("Error: Please provide a valid audio file (mp3, wav, ogg, or m4a).")
            continue
            
        return file_path

def transcribe_audio(file_path, language):
    """
    Transcribe audio file using Sunbird AI API.
    Returns the transcribed text or an error message.
    """
    try:
        # Prepare the request
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {AUTH_TOKEN}",
        }

        # Get file name from path
        file_name = os.path.basename(file_path)

        # Prepare the files and data
        files = {
            "audio": (
                file_name,
                open(file_path, "rb"),
                "audio/mpeg",
            ),
        }
        
        data = {
            "language": LANGUAGE_CODES[language],
            "adapter": LANGUAGE_CODES[language],
            "whisper": True,
        }

        # Make the API request
        response = requests.post(API_URL, headers=headers, files=files, data=data)
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            # The API returns the transcription in 'audio_transcription' field
            if 'audio_transcription' in result:
                return result['audio_transcription']
            return "Transcription not available"
        else:
            error_msg = response.text
            return f"Error: API returned status code {response.status_code}. Details: {error_msg}"

    except requests.exceptions.RequestException as e:
        return f"Error connecting to the API: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    finally:
        # Make sure to close the file
        if 'files' in locals():
            files['audio'][1].close()

def main():
    """
    Main function to run the transcription process.
    Handles user interaction and transcription process.
    """
    print("\nWelcome to the Audio Transcription Tool!")
    print("This tool helps transcribe audio files in English and local Ugandan languages.")
    print("=" * 50)
    
    # Get audio file path
    file_path = get_audio_file_path()
    
    # Get source language (language of the audio)
    source_language = get_language_input(
        "\nWhat language is the audio in?\n"
        "(Choose one of: English, Luganda, Runyankole, Ateso, Lugbara or Acholi): "
    )
    
    # Get target language (language for the transcription)
    target_language = get_language_input(
        "\nWhat language do you want the transcription in?\n"
        "(Choose one of: English, Luganda, Runyankole, Ateso, Lugbara or Acholi): "
    )
    
    # Transcribe and show result
    print(f"\nTranscribing audio from {source_language} to {target_language}...")
    transcription = transcribe_audio(file_path, source_language)
    
    # If the transcription is in a different language than requested, translate it
    if source_language != target_language:
        print("\nTranslating the transcription...")
        from translate import translate_text
        transcription = translate_text(source_language, target_language, transcription)
    
    print(f"\nAudio transcription text in {target_language.lower()}:")
    print(transcription)
    print("\nThanks for using the transcription tool!")

if __name__ == "__main__":
    main() 