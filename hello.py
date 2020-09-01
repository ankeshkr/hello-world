import pickle
def answer(name):
  return "Hello" + str(name)


a="ankesh"

res=answer(a)
#print (res)
pickle.dump(res, open('hello2.pkl','wb'))

# Loading model to compare the results
hello = pickle.load(open('hello2.pkl','rb'))
print (hello)
