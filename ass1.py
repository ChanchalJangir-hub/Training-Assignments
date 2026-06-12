#                    Topic-Basic Python
#                 ******Assignment-1******

# Solution-1

# a.Integer(int) -> An integer is a built-in data type used to store positive , negative or zero without decimals.
# Example:-
_positive = 10
_negative = -12
_zero = 0
print(type(_positive))
print(type(_negative))
print(type(_zero))

# b.Float(float) -> A float data type is used to store decimal value(like-positive ,negative or zero).
# Example:-
positive = 10.2
negative = -53.0
zero = 0.00
print(type(positive))
print(type(negative))
print(type(zero))

# c.String(str) -> A string is a sequence of characters and also digits enclosed in quotes.
# Example:-
str = "hello"
str1 = "1234"
print("Characters string:",str)
print("Digits string:",str1)
print(type(str))
print(type(str1))

# d.Boolean(bool) -> A boolean  is a built-in data type it represents one or two posible values(True,False).It belongs to bool class mostly used in-conditions , loops and comparision.
# Example:- 
a = True
b = False
print("a =",a ,type(a))
print("b =",b ,type(b))


# Solution-2

name = "Gargi"
age = 20
city = "Jaipur"

print("Name:",name) # Name:Gargi
print("Age:",age)   # age:20
print("City:",city) # city:Jaipur


# Solution-3

name = input("Enter your name:") 
print("Uppercase Name:",name.upper())
print("Total number of character:",len(name)) 


# Solution-4

# a.count() -> count()  refers to the built-in.count() method , which finds the number of times a specific value appears within a sequence like-string,list or tuple.

str ="hello "
print(str.count("l")) # 2

# b.title() -> Uppercase the first character of every word.

str = "python programming"
print(str.title()) # Python Programming

# c.strip() -> strip() is used to remove leading and trailing characters from a string.

str =" hello "
print(str.strip()) # hello

# d.upper() -> Converts all characters to uppercase.

str = "python"
print("Uppercase String:",str) # PYTHON


# e.lower() -> Converts all characters to lowercase.
str = "PYTHON"
print("Lowercase String:",str) # python 

# Solution-5

lst = ["Apple","Mango","litchi","Strawberry","Guava"]
print(lst)
print("first element:",lst[0],"and","Last element:",lst[-1]) # ['Apple','Guava']
print(len(lst)) # 5


# Solution-6

lst = [10 , 20 , 30 , 40 , 50]
lst.append(60) 
lst.remove(20)
print(lst) # [10 , 30 , 40 , 50 ,60]


# Solution-7

# Artificial Intelligence (AI):-  Artificial Intelligence is a branch of computer science that focuses on creating machines and software capable of performing tasks that normally require human intelligence. These tasks include learning, reasoning, problem-solving, decision-making, understanding language, and recognizing patterns(it works as a human brain).Also perform task automatically without any support by human and other resouces.

# **Importance of AI**

# Automation:- Reduces human effort by automating repetitive tasks.
# Efficiency:- Performs tasks faster and with greater accuracy.
# Better Decision-Making:- Analyzes large amounts of data to provide useful insights.
# 24/7 Availability:- AI systems can work continuously without breaks.
# Improved User Experience:- Provides personalized recommendations and assistance.


# **Four Real-Life Applications of AI**

# 1.Chatbots and Virtual Assistants – ChatGPT, Alexa, Siri, and Google Assistant.
# 2.Recommendation Systems – Netflix, YouTube, and Amazon suggest content/products based on user preferences.
# 3.Healthcare – AI helps doctors diagnose diseases and analyze medical images.
# 4.Navigation and Traffic Prediction – Google Maps uses AI to suggest the fastest routes and predict traffic conditions.


# Solution-8

# * ChatGPT:- ChatGPT is an AI-powered chatbot that uses machine learning and natural language processing (NLP) to understand human language and generate human-like responses. It can answer questions, write text, solve problems, and learn patterns from large amounts of data.

# Example:- When a user asks a question, ChatGPT analyzes the input and generates a relevant response, similar to how a human would communicate.

# * Google Maps route prediction:- Google Maps uses AI to analyze real-time traffic data, road conditions, historical travel patterns, and user location data. Based on this information, it predicts the fastest route and estimated travel time.
#  Example:- If you are traveling from Jaipur to Delhi, Google Maps may suggest different routes. It can detect traffic jams, road closures, or accidents and recommend an alternative route to help you reach your destination faster.

# * Calculator:- A calculator follows predefined mathematical rules and instructions programmed by humans. It does not learn from data, make decisions, or improve its performance over time. It simply performs calculations based on the input provided.
# Example:- If you enter 25 + 15, the calculator will always return 40 using fixed mathematical operations. It cannot understand context, predict outcomes, or learn new skills.

# * Netflix recommendations:- Netflix uses AI and machine learning algorithms to analyze a user's viewing history, ratings, watch time, and preferences. Based on this data, it recommends movies and TV shows that the user is likely to enjoy.
# Example:- If you frequently watch action movies and crime dramas, Netflix may recommend similar content such as action thrillers or detective series. The recommendations become more personalized as you continue watching.

# * Voice assistants (Alexa/Siri):- Alexa and Siri use Artificial Intelligence, Natural Language Processing (NLP), and Machine Learning to understand spoken language, process user requests, and provide appropriate responses. They can recognize voice commands, answer questions, set reminders, play music, and perform many other tasks.
# Example:- If you say, "Alexa, play my favorite songs" or "Siri, set an alarm for 6 AM," the assistant understands your voice command and performs the requested action au