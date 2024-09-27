import speech_recognition as sr
import spacy
import pyttsx3
import numpy as np
from scipy.signal import find_peaks

# Initialize speech recognition, NLP, and text-to-speech engines
recognizer = sr.Recognizer()
nlp = spacy.load("en_core_web_sm")
engine = pyttsx3.init()

# Function for stress detection (mock-up using pitch analysis)
def detect_stress(audio_signal):
    # Dummy function, replace with actual pitch analysis or AI model
    peaks, _ = find_peaks(audio_signal, height=0.5)
    if len(peaks) > 5:  # Example threshold for high stress
        return "High"
    return "Normal"

# Function to listen and convert speech to text
def listen_to_driver():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Command: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError:
        print("Service unavailable")
        return None

# Function to analyze and respond to commands
def process_command(command):
    doc = nlp(command)
    
    if "sleepy" in command or "tired" in command:
        # Simulate analyzing the audio signal for stress
        stress_level = detect_stress(np.random.rand(100))  # Replace with real audio signal
        if stress_level == "High":
            engine.say("You seem stressed. Please take a break.")
            engine.runAndWait()
        else:
            engine.say("Take care. Would you like me to find a rest stop nearby?")
            engine.runAndWait()
    elif "route" in command or "directions" in command:
        engine.say("Where would you like to go?")
        engine.runAndWait()
    elif "SOS" in command or "help" in command:
        engine.say("Sending SOS signal and notifying emergency services.")
        engine.runAndWait()
    else:
        engine.say("I'm here to help. Please tell me what you need.")
        engine.runAndWait()

# Main loop to keep the bot running
def main():
    while True:
        command = listen_to_driver()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
