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

from Move import Move

from GameManager import GameManager

from BadHandicapError import BadHandicapError
size=int(config['GOBAN']['size'])
if not size in [9,13,19] :
    raise BadHandicapError("")

handicap=int(config['HANDICAP']['number_of_stones'])
my_game_manager=GameManager(size,handicap)

r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()

blindfolded_player_is_black=my_game_manager.is_blindfolded_player_black()
blindfolded_player_starts=my_game_manager.blindfolded_player_starts(handicap)
label_dict={True:"black", False:"white"}
os.system("say 'Blindfolded player plays with the "+label_dict[blindfolded_player_is_black]+" stones !'") 
os.system("say 'Game started !'")

if not blindfolded_player_starts:
    move_from_AI=my_game_manager.request_move_from_AI()
    my_game_manager.play_move(move_from_AI)
    os.system("say '"+label_dict[blindfolded_player_is_black==False]+" plays "+move_from_AI.get_go_name()+" !'")

while(my_game_manager.is_game_over()==False):
    my_game_manager.print_position()
    is_playable_move=False
    is_move=False
    result=""
    
    while(is_move==False):
        while(is_playable_move==False):
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                result=r.recognize_google(audio)
                result=result.upper() # the upper function is used so that 'd2' becomes 'D2' and is recognized as a move
                result=result.replace(" ", "") # the replace function is used so that 'A 2' becomes 'A2' then and is recognized as a move

            except sr.UnknownValueError:
                # speech was unintelligible
                result=""

            if result == "":
                is_playable_move=False
                is_move=False
            else:
                is_move=GameManager.is_move(result,size)
                if is_move==False: 
                    is_playable_move=False
                else: 
                    is_playable_move=my_game_manager.is_playable_move(Move(result))

    move=Move(result)
    my_game_manager.play_move(move)

    #my_game_manager.is_playable_move(move)
    if result == "pass":
        os.system("say '"+label_dict[blindfolded_player_is_black]+" passes !'")
    elif result == "resign":
        os.system("say '"+label_dict[blindfolded_player_is_black]+" resigns !'") 
    else:
        os.system("say '"+label_dict[blindfolded_player_is_black]+" plays "+result+" !'") 
    '''
    else:
        os.system("say 'This move can't be played !'")
    '''

    if my_game_manager.is_game_over():
        break
    else:
        move_from_AI=my_game_manager.request_move_from_AI()
        my_game_manager.play_move(move_from_AI)
        os.system("say '"+label_dict[blindfolded_player_is_black==False]+" plays "+move_from_AI.get_go_name()+" !'")



os.system("say 'Thanks for the game !'")