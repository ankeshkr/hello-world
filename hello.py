import pickle
def answer(name):
  print("Hello" + name)

a=input("what is your name")
print (a)
answer(a)
pickle.dump(answer, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
