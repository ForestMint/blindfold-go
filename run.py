
import sente

import speech_recognition as sr


import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# speak structure for non-Debian OSs
'''
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
'''

# speak structure for Debian Oss
'''
import espeak
espeak.init()
speaker = espeak.Espeak()
speaker.say("Hello world")
speaker.rate = 300
speaker.say("Faster hello world")
'''

import sys
sys.path.append('./python_classes')

import os

from GameManager import GameManager
size=int(config['GOBAN']['size'])
handicap=int(config['HANDICAP']['number_of_stones'])
my_game_manager=GameManager(size,handicap)

r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()

blindfolded_player_is_black=my_game_manager.is_blindfolded_player_black()
label_dict={True:"black", False:"white"}
os.system("say 'Blindfolded player plays with the "+label_dict[blindfolded_player_is_black]+" stones !'") 
os.system("say 'Game started !'")

if not blindfolded_player_is_black:
    move_from_AI=my_game_manager.request_move_from_AI()
    os.system("say 'White plays "+move_from_AI+" !'")


while(my_game_manager.is_game_over()==False):

    result=""

    while(GameManager.is_move(result,size)==False):
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            result=r.recognize_google(audio)
        except sr.UnknownValueError:
            # speech was unintelligible
            result=""



    if my_game_manager.is_playable_move(result):
        my_game_manager.play_move(result)
        if result == "pass":
            os.system("say '"+label_dict[blindfolded_player_is_black]+" passes !'")
        elif result == "resign":
            os.system("say '"+label_dict[blindfolded_player_is_black]+" resigns !'") 
        else:
            os.system("say '"+label_dict[blindfolded_player_is_black]+" plays "+result+" !'") 
    else:
        os.system("say 'This move can't be played !'")

    if my_game_manager.is_game_over():
        break
    else:
        move_from_AI=my_game_manager.request_move_from_AI()
        os.system("say '"+label_dict[blindfolded_player_is_black==False]+" plays "+move_from_AI+" !'")


    print(result)

os.system("say 'Thanks for the game !'")
