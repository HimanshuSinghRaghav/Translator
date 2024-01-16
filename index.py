import streamlit as st
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def main():
    st.title("Text Translator ")

    # Input box for user to enter text
    input_text = st.text_area("Enter text to translate:")

    # Mapping of language codes to full names
    language_mapping = {
        "en": "English",
        "hi": "Hindi",
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "ja": "Japanese",
        "ko": "Korean",
        "pt": "Portuguese",
        "ru": "Russian",
    }

    # Create a list of language names for display in the select box
    language_names = [f"{name} ({code})" for code, name in language_mapping.items()]

    # Select box for choosing the target language
    target_language_index = st.selectbox("Select target language:", range(len(language_names)), format_func=lambda x: language_names[x])

    # Get the selected language code from the index
    target_language = list(language_mapping.keys())[target_language_index]

    # Button to trigger translation
    if st.button("Translate"):
        if input_text:
            translated_text = translate_text(input_text, target_language)
            st.text_area("Translated text:", translated_text)

if __name__ == "__main__":
    main()
