import pickle
def answer(name):
  print("Hello" + name)

a=input("what is your name")
print (a)
answer(a)
pickle.dump(answer, open('hello.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('hello.pkl','rb'))
