#!/usr/bin/env python3
"""
A simple translator for Ugandan languages using Sunbird AI API.
This script helps translate between English and 5 local Ugandan languages.
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API configuration
API_URL = "https://api.sunbird.ai/tasks/nllb_translate"
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

def translate_text(source_lang, target_lang, text):
    """
    Translate text using Sunbird AI API.
    Returns the translated text or an error message.
    """
    try:
        # Prepare the request
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {AUTH_TOKEN}",
            "Content-Type": "application/json",
        }

        data = {
            "source_language": LANGUAGE_CODES[source_lang],
            "target_language": LANGUAGE_CODES[target_lang],
            "text": text
        }

        # Make the API request
        response = requests.post(API_URL, headers=headers, json=data)
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            # The API returns the translation in result['output']['translated_text']
            if 'output' in result and 'translated_text' in result['output']:
                return result['output']['translated_text']
            return "Translation not available"
        else:
            error_msg = response.text
            return f"Error: API returned status code {response.status_code}. Details: {error_msg}"

    except requests.exceptions.RequestException as e:
        return f"Error connecting to the API: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    """
    Main function to run the translator.
    Handles user interaction and translation process.
    """
    print("\nWelcome to the Ugandan Language Translator!")
    print("This tool helps you translate between English and local Ugandan languages.")
    print("=" * 50)
    
    # Get source language
    source_lang = get_language_input(
        "\nWhat language are you translating from?\n"
        "(Choose one of: English, Luganda, Runyankole, Ateso, Lugbara or Acholi): "
    )
    
    # Get target language
    while True:
        target_lang = get_language_input(
            "\nWhat language do you want to translate to?\n"
            "(Choose one of: English, Luganda, Runyankole, Ateso, Lugbara or Acholi): "
        )
        if target_lang != source_lang:
            break
        print("Hmm... You can't translate to the same language. Try a different one!")
    
    # Get text to translate
    text = input("\nWhat would you like to translate? ").strip()
    
    # Translate and show result
    print("\nTranslating...")
    translation = translate_text(source_lang, target_lang, text)
    print(f"\nTranslation: {translation}")
    print("\nThanks for using the translator!")

if __name__ == "__main__":
    main() 