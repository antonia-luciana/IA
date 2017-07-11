import pickle, zipfile, numpy
from keras.models import Sequential

model = Sequential()
with open('letter-recognition.data','r') as f:
    letters = f.read()
    print (letters)
    f.close()

def parsare(text):
    return  text.split[',']

print parsare(letters)