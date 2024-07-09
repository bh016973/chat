import nltk
from nltk.chat.util import Chat,reflections

pairs =[
    [
    r"hi|hey|hello",
    ["hello!","hey there!","hi!how can i assist you?"]
    ],
[
    r"what is your name?",
    ["you can call me chat bot.","i'm chatbot,nice to meet you!"]
    ],
        [
            r"my name is(.*)",
            ["hello %1,how are you today?"]
            ],
        [
            r"how are you?",
            ["i'm good.how about you?"]
            ],
        [
            r"who are you?",
            ["this is chatbot!"]
            ],
    [
        r"do you know me?",
        ["ohh! yes!","you are bhargavi!","right!"]
        ],
    [
            r"can you answer my questons?",
            ["ohh!","what is your question?"]
            ],
        [
            r"bye",
            ["bye!take care.","goodbye! have a great day!"]
            ],
        [
            r"(.*)",
            ["sorry,i didn't understand that."]
            ]
    ]
chatbot=Chat(pairs,reflections)
chatbot.converse()
