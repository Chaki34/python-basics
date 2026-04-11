# Step 1: Import the pyttsx3 library (used for text-to-speech)
import pyttsx3


# Step 2: Initialize the speech engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')

# Print all available voices
for i, voice in enumerate(voices):
    print(i, voice.name, voice.id + "\n")

# Step 3: Take input from the user
text = input("Enter a sentence: ")

# Step 4: Set speech speed (rate of speaking)
# Default is around 200, lower = slower voice
engine.setProperty('rate', 150)

# Step 5: Set volume level (0.0 to 1.0)
# 1.0 means full volume
engine.setProperty('volume', 1.0)


# if want to set spacific voice like male or female 

#for male voice (usually index 0, but depends on system)
# Female voice (usually index 1, but depends on system)
engine.setProperty('voice', voices[1].id)



# Step 6: Add the text to speech queue
engine.say(text)

# Step 7: Run the speech engine and speak the text
engine.runAndWait()