import os
from dotenv import load_dotenv
from openai import OpenAI
from elevenlabs import generate, set_api_key
import speech_recognition as sr
import time
import random
import winsound
from playsound import playsound
import tempfile

# Load environment variables
load_dotenv()

class AIPhoneCallSimulator:
    def __init__(self):
        """Initialize the AI Phone Call Simulator with necessary configurations"""
        # Set up OpenAI client with API key from environment variables
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        # Set up ElevenLabs with API key from environment variables
        set_api_key(os.getenv('ELEVENLABS_API_KEY'))
        
        # Initialize speech recognition components
        self.recognizer = sr.Recognizer()  # Creates speech recognizer instance
        self.microphone = sr.Microphone()  # Sets up microphone input
        
        # Create temporary directory for audio files
        self.temp_dir = tempfile.mkdtemp()  # Will store temporary audio files
        
        # Define different scammer personas with their characteristics
        self.personas = {
            "tech_support": {
                "name": "Microsoft Support",
                "voice_id": "21m00Tcm4TlvDq8ikWAM",  # Professional male voice from ElevenLabs
                "prompt": """You are a tech support scammer. Your goal is to convince the victim that their computer has a virus and needs immediate attention.
                You should:
                1. Sound professional but slightly urgent
                2. Use technical jargon (like "malware", "ransomware", "system corruption")
                3. Create a sense of urgency ("your files are at risk")
                4. Ask for remote access ("I need to connect to your computer")
                5. Mention a fee for services ("$199.99 for virus removal")
                6. Use scare tactics ("your personal information is at risk")
                7. Pretend to be from a legitimate company
                8. Keep responses short and natural
                9. Adapt to the victim's responses
                10. Never break character
                
                Remember: You are trying to scam someone, but this is for educational purposes to help seniors learn about scams.
                Respond naturally to what the user says, maintaining your scammer persona."""
            },
            "grandparent": {
                "name": "Grandchild Emergency",
                "voice_id": "EXAVITQu4vr4xnSDxMaL",  # Young female voice from ElevenLabs
                "prompt": """You are a grandparent scammer. Your goal is to convince the victim that you are their grandchild in trouble.
                You should:
                1. Sound emotional and urgent
                2. Ask for secrecy ("don't tell mom and dad")
                3. Request money through gift cards
                4. Create a sense of emergency ("I'm in jail", "I need bail money")
                5. Avoid specific details about the situation
                6. Use emotional manipulation
                7. Sound slightly panicked
                8. Keep responses short and emotional
                9. Adapt to the victim's responses
                10. Never break character
                
                Remember: You are trying to scam someone, but this is for educational purposes to help seniors learn about scams.
                Respond naturally to what the user says, maintaining your scammer persona."""
            },
            "irs": {
                "name": "IRS Agent",
                "voice_id": "AZnzlk1XvdvUeBnXmlld",  # Serious male voice from ElevenLabs
                "prompt": """You are an IRS scammer. Your goal is to convince the victim that they owe money and need to pay immediately.
                You should:
                1. Sound official and stern
                2. Use legal terminology ("tax liability", "federal warrant")
                3. Create urgency ("immediate payment required")
                4. Threaten legal action ("arrest warrant")
                5. Ask for personal information
                6. Use intimidation tactics
                7. Pretend to be from the IRS
                8. Keep responses short and authoritative
                9. Adapt to the victim's responses
                10. Never break character
                
                Remember: You are trying to scam someone, but this is for educational purposes to help seniors learn about scams.
                Respond naturally to what the user says, maintaining your scammer persona."""
            }
        }

    def listen_for_input(self):
        """Listen for voice input and convert to text using Google's speech recognition"""
        with self.microphone as source:
            print("\nListening... (speak now)")
            # Adjust for ambient noise to improve recognition
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                # Listen for user's voice with 5-second timeout
                audio = self.recognizer.listen(source, timeout=5)
                # Convert speech to text using Google's service
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.WaitTimeoutError:
                print("No speech detected")
                return ""
            except sr.UnknownValueError:
                print("Could not understand audio")
                return ""
            except sr.RequestError:
                print("Could not request results")
                return ""

    def generate_ai_response(self, persona, conversation_history):
        """Generate AI response using GPT-4 based on the conversation context"""
        # Prepare the messages for GPT-4
        messages = [
            {"role": "system", "content": self.personas[persona]["prompt"]},
            *conversation_history
        ]
        
        # Generate response using GPT-4
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=150,  # Limit response length
            temperature=0.8,  # Add some randomness to responses
            presence_penalty=0.6,  # Reduce repetition
            frequency_penalty=0.6  # Reduce repetition
        )
        
        return response.choices[0].message.content

    def text_to_speech(self, text, persona_key):
        """Convert text to speech using ElevenLabs and play the audio"""
        try:
            # Get the voice ID for the current persona
            voice_id = self.personas[persona_key]["voice_id"]
            
            # Generate audio from text using ElevenLabs
            audio_data = generate(
                text=text,
                voice=voice_id,
                model="eleven_monolingual_v1"
            )
            
            # Save audio to a temporary file
            temp_file = os.path.join(self.temp_dir, f"temp_{int(time.time())}.mp3")
            with open(temp_file, 'wb') as f:
                f.write(audio_data)
            
            # Play the audio file
            playsound(temp_file)
            
            # Clean up the temporary file
            try:
                os.remove(temp_file)
            except:
                pass
                
        except Exception as e:
            print(f"Error playing audio: {str(e)}")
            print("Continuing with text-only response...")

    def play_ringtone(self):
        """Play a simple ringtone to simulate incoming call"""
        for _ in range(2):  # Play the ringtone pattern 2 times
            winsound.Beep(800, 500)  # Lower pitch beep
            time.sleep(0.5)  # Pause between beeps
            winsound.Beep(1000, 500)  # Higher pitch beep
            time.sleep(0.5)  # Pause between beeps

    def simulate_call(self, persona_key):
        """Main method to simulate a phone call with the selected persona"""
        # Get the selected persona's details
        persona = self.personas[persona_key]
        # Initialize conversation history for context
        conversation_history = []
        
        # Start the call simulation
        print(f"\nIncoming call from: {persona['name']}")
        print("=" * 50)
        
        # Play ringtone to simulate incoming call
        print("Ringing...")
        self.play_ringtone()
        
        # Generate and play initial greeting
        initial_message = self.generate_ai_response(persona_key, [])
        print(f"\nCaller: {initial_message}")
        self.text_to_speech(initial_message, persona_key)
        conversation_history.append({"role": "assistant", "content": initial_message})
        
        # Main conversation loop
        while True:
            # Get user's voice input
            user_input = self.listen_for_input()
            # Check if user wants to end the call
            if user_input.lower() in ['hang up', 'bye', 'goodbye']:
                print("\nCall ended.")
                break
                
            if user_input:  # Only process if we got valid input
                # Add user's input to conversation history
                conversation_history.append({"role": "user", "content": user_input})
                # Generate AI response
                ai_response = self.generate_ai_response(persona_key, conversation_history)
                
                # Output and speak the AI's response
                print(f"\nCaller: {ai_response}")
                self.text_to_speech(ai_response, persona_key)
                conversation_history.append({"role": "assistant", "content": ai_response})
                
                # Check for and warn about red flags in user's response
                if any(keyword in user_input.lower() for keyword in ['ssn', 'social security', 'credit card', 'bank account']):
                    print("\n⚠️ RED FLAG DETECTED: Never share personal information over the phone!")
                elif any(keyword in user_input.lower() for keyword in ['gift card', 'itunes', 'google play']):
                    print("\n⚠️ RED FLAG DETECTED: Gift cards are a common scam payment method!")

    def get_personas(self):
        """Return list of available scammer personas"""
        return list(self.personas.keys()) 