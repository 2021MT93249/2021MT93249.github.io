# importing textblob library
from textblob import TextBlob 

t = 1
while t:
    a = input("Enter the word to be checked:- ")	 # wrong spelling
    print("original text: "+str(a))     #print the original text

    b = TextBlob(a)  #correct the text

    print("corrected text: "+str(b.correct()))
    t = int(input("Try Again? 1 : 0 "))