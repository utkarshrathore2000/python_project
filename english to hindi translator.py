from textblob import TextBlob
english=input('enter your text')
word=TextBlob(english)
z=word.translate(from_lang='en',to ='hi')
print(z)
