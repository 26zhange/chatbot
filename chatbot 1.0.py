import time
import string
import math
import random
class main():
    print("Hi, this is Chatbot 1.0")
    bot_response = ""

    #dictionaries and array for conversation words
    responses = {
        "hi":"hi,tell me a little bit about yourself",
        "when where you born" : "I forgot",
        "hello":"hello, tell me a little bit about yourself",
        "what is your name":"My name is chatbot",
        "how are you":"I am well",
        "what is your favorite color":"My favorite color is blue",
        "do you like" : "Yes" or "no"


        }
    bot_question = ["What's your name?","How are you?","What's your favorite color","How old are you?"]
    numbers = {
        "one": 1,
        "two":2,
        "three":3
        }

    #fuctions of user input
    what_user_likes = []
    user_input = ""
    while  user_input != "bye":
        user_input = input("user:")
        message = user_input.lower()
        if '?' or '.' in user_input:
            message = message.replace('?',"")
            message = message.replace('.',"")
        if "what's" in user_input:
        
            
            time.sleep(1)
            message = message.replace("what's", "what is")
        if message in responses:
            time.sleep(1)
            print("bot:"+ responses[message])
        elif "do you like" in message:
            time.sleep(1)
            message = "do you like"
            print("bot:" + responses[message])
        elif message == "bye":
            time.sleep(1)
            print("bot: bye")
            break

        elif "my name is " in message:
            time.sleep(1)
            message = message.replace("my name is","")
            name = message
            print("bot: Cool name"+name+",tell me more")
        elif "I am" and "years old" in message:
            message = message.replace("I am"and"years old", "")
            age = message
            print("bot: tell me more")
        elif "How are you?" in bot_question and "i am" in message:
            message = message.replace("i am","")
            user_emotion = message
        elif "i like" in message:
            message = message.replace("i like","")
            what_user_likes = what_user_likes.append(message)
            print("bot: I also like"+message)
        else:
            print("bot:"+ random.choice(bot_question) )
