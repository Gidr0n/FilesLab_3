import json
import pickle
import pandas as pd
from bs4 import BeautifulSoup
import lxml
#1
with open("addres-book.json", "r") as read_file:
    data = json.load(read_file)
for i in range(len(data)):
    l1st = data[i]['email']
print(*l1st)
#2
for i in range(len(data)):
  l1st=data[i]['phones']
print(*l1st)
#3
l1st=[]
with open('addres-book-q.xml') as f:
    BS=BeautifulSoup(f,'xml')
for el in BS.address_book.find_all('address'):
    x=[x.next for x in el.phones.find_all('phone')]
    l1st.append({el.find('name').next:x})
print(l1st)
# Лабораторная работа №4
# JSON
#1.1
with open("contributors_sample.json", "r") as read_file:
    data = json.loads(read_file.read())
    print(*data[0:3])
#1.2
l1st=[]
for i in range(len(data)):
    y=data[i]['mail']
    y=y.split('@')
    l1st.append(x[1])
print(set(l1st))
#1.3
def name(username):
  for i in range(len(data)):
    y = data[i]['username']
    if username==y:
      print(data[i])
      break
    else:
      continue
  else:
    raise ValueError
print(name('uhebert'))
#1.4
for i in range(len(data)):
  if data[i]['sex']=='F':
    l1stf=data[i]['sex']
for i in range(len(data)):
  if data[i]['sex']=='M':
    l1stm=data[i]['sex']
print(len(l1stf))
print(len(l1stm))
#1.5
l1st1=[]
for i in range(len(data)):
        l1st = [[], [], []]
        x,y,z = data[i]['username'],data[i]['id'],data[i]['sex']
        l1st[0],l1st[1],l1st[2]=x,y,z
        l1st1.append(l1st)
contributers=pd.DataFrame(l1st1,columns=['name','id','sex'])
#1.6
recipes = pd.read_csv("recipes_sample.csv",sep=',',header=0)
recipes=pd.concat([recipes,contributers])
recipes=recipes.dropna(subset='id')
print(recipes)
# pickle
#2.1
l1st1={}
l1st0={}
l1st_job=[data[i]['jobs'] for i in range(len(data))]
l1st_names=[data[i]['username'] for i in range(len(data))]
st=[data[i]['jobs'] for i in range(len(data))]
for i in range(len(st)):
    for j in range(len(st[i])):
        x=[]
        for k in range(len(data)):
            if st[i][j] in data[k]['jobs']:
                x.append(data[k]['username'])
                l1st0={st[i][j]:x}
                l1st1.update(lst0)
print(l1st1)
#2.2
with open('job_people.pickle','wb') as w:
    pickle.dump(l1st1,w)
with open('job_people.json','w') as w1:
    json.dump(l1st1,w1)
#2.3
with open('job_people.pickle','rb') as r:
  data_new=pickle.load(r)
  print(data_new)
# XML
#3.1
with open('steps_sample.xml') as f:
    BS=BeautifulSoup(f,'xml')
res=list()
print(BS.steps)
for el in BS.find_all('recipe'):
    steps=el.steps.text
    steps=steps.split('\n')
    res.append({el.find('id').next:steps[1:3]})
with open('steps_sample.json','w') as w:
    json.dump(res,w
#3.2
with open('steps_sample.xml') as f:
    BS=BeautifulSoup(f,'xml')
res=list()
d1tc={}
d1tc0={}
l=[len(el.steps.text.split('\n'))-1 for el in BS.find_all('recipe')]
y=BS.find_all('recipe')
for j in range(len(l)):
    l1st1=[]
    for i in range(len(x)):
            steps = y[i].steps.text
            steps_lght=len(steps.split('\n'))-1
            if steps_lght==l[j]:
                l1st1.append(y[i].find('id').next)
    d1tc0={steps_lght:l1st1}
    d1tc.update(d1tc0)
print(d1tc)
#3.3
l1st=[]
with open('steps_sample.xml') as f:
    BS=BeautifulSoup(f,'xml')
for i in BS.find_all('recipe'):
    y=list(i.step.parent)
    for j in x:
        j=str(j)
        if '<step has_minutes="1">' in j:
            l1st.append(i)
#3.4
with open('steps_sample.xml') as f:
    BS=BeautifulSoup(f,'xml')
l=[len(el.steps.text.split('\n'))-1 for el in BS.find_all('recipe')]
recipe=pd.read_csv('recipes_sample.csv')
print(recipe)
recipe.n_steps = recipe.n_steps.fillna('XXXX')
for i in range(len(recipe['n_steps'])):
    if recipe['n_steps'][i]== 'XXXX':
        recipe['n_steps'][i]=l[i]
    print(recipe['n_steps'][i])
#3.5
print(recipe.n_steps.isna().sum())
recipe.n_steps=recipe.n_steps.astype(int)
recipe=recipe.to_csv('recipes_sample_with_filled_nsteps.csv')
