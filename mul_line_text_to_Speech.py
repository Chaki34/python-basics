import pyttsx3

import time
engine = pyttsx3.init()
engine.setProperty('rate', 150)

texts = ["Hello", "Welcome", "To Python"]

for word in texts:
    engine.say(word)

engine.runAndWait()

time.sleep(3)  # keep program alive a bit longer importnet for buffring purpouse to make the program alive 