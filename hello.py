import pickle
def answer(name):
  return "Ankesh " + str(name)


a="kr"

res=answer(a)
#print (res)
pickle.dump(res, open('hello3pkl','wb'))

# Loading model to compare the results
hello = pickle.load(open('hello3.pkl','rb'))
print (hello)
