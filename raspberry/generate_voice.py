from gtts import gTTS
import os

tts_photo = gTTS(text="Merci d'avoir utilise cycle" , lang='fr')
tts_photo.save("sounds/generated/merci.mp3")



