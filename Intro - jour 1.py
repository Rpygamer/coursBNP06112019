#!/usr/bin/env python
# coding: utf-8

# In[8]:


ma_variable = 3

ma_variable = "Bonjour"

print(ma_variable)
print("ma_variable")


# ## Titre
# 
# #### Sous titre
# 
# Ceci est un paragraphe
# 
# * Item 1
# * Item 2
# * Item 3

# In[12]:


ma_variable = "Bonjour"
ma_variable = 42
ma_variable = 4.2
ma_variable = 4 + 2j
ma_variable = True
ma_variable = False
ma_variable = None


print(type(ma_variable))


# In[21]:


a = 2
b = 4

a = 5
a += 1 # a = a + 1

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

print(True and False)
print(True or False)

c = 5
c


# In[26]:


age = 56

condition1 = age > 18
condition2 = age < 40
condition3 = age == 18
condition4 = age != 40

print(condition1)
print(condition2)

print(condition1 and condition2) # age doit satisfaire les deux conditions
print(condition1 or condition2) # age doit satisfaire les deux conditions


# In[30]:


ma_liste = [2,5,1,6]
print(ma_liste[0]) # Premier element
print(ma_liste[1]) # Deuxième element
print(ma_liste[3]) # 4e element
print(ma_liste[-1]) # Dernier element
print(ma_liste[-2]) # Avant dernier element


# In[41]:


ma_liste = [2,5,1,6]
liste_copy = ma_liste # reference la même liste dans une autre variable
liste_copy = list(ma_liste) # crée une copie de ma liste
liste_copy = ma_liste.copy() # crée une copie de ma liste
print(len(ma_liste))
print(ma_liste.index(5))
print(max(ma_liste))
print(min(ma_liste))
liste_copy.sort()
print(ma_liste)


# In[46]:


# help(ma_liste)
# dir(ma_liste)
# help(ma_liste.append)


# In[52]:


ma_liste = [True, None, 4, 6, 32]

ma_liste.append(7)
ma_liste.append([12, 13])
ma_liste.extend([12, 13])
ma_liste.pop(0)
ma_liste += [12, 13]

ma_liste


# In[54]:


ma_liste = [0] * 100
print(ma_liste)
ma_liste = [] # Création de liste vide


# In[60]:


# Slicing
ma_liste = [True, None, 4, 6, 32, 7, 13, 12, [15, 16]]

# Récupérer le dernier elmt du dernier elmt de ma_liste
print(ma_liste[-1][-1]) 

print(ma_liste[0:2])
print(ma_liste[1:4])
print(ma_liste[:2])
print(ma_liste[2:])
print(ma_liste[2:-1])
print(ma_liste[0:6:2])
print(ma_liste[::-2])


# In[62]:


# Exercice

ma_liste = [True, None, 4, 6, 32, 7, 13, 12, [15, 16]]

# Récupérer le premier element
print(ma_liste[0])
# Récupérer dernier élément
print(ma_liste[-1])
# Récupérer le premier element de la liste [15, 16] (à la fin)
print(ma_liste[-1][0])
# Récupérer un élément sur deux
print(ma_liste[::2])
# Récupérer du 2e au 6e inclus
print(ma_liste[1:6])
# Récupérer du 2e à la fin de 2 en 2
print(ma_liste[1::2])
# Récupérer de l'avant dernier au troisième
print(ma_liste[-2:1:-1])


# In[68]:


personne = {"nom": "Dupont", "prenom": "Elise", "age": 37, True: [1,5,7]}
personne["nom"]

personne1 = {"nom": "Dupont", "prenom": "Elisa", "age": 37, True: [1,5,7]}
personne2 = {"nom": "Dupont", "prenom": "Martin", "age": 37, True: [1,5,7]}

table_notes_eleves = {
    12: personne1,
    16: personne2
}

table_notes_eleves[12]["nom"]


# In[69]:


# liste (liste_personnes) qui contient personne, personne1 et personne2
liste_personnes = [personne, personne1, personne2]
# afficher le nom de la premiere personne de la liste
print(liste_personnes[0]["nom"])
# afficher le prenom de la dernière personne de la liste
liste_personnes[-1]["prenom"]
# ajouter une personne que vous créez dans la liste
personne_a_ajouter = {"nom": "Durand", "prenom": "Thomas", "age": 32}
liste_personnes.append(personne_a_ajouter)


# In[75]:


personne["nom"] = "Helene"
print(liste_personnes[0]["nom"])

mon_tuple = (1, 8, 4, 12)
# mon_tuple[0] = 2
mon_tuple = (2,) + mon_tuple[1:]
mon_tuple


# In[ ]:





# In[65]:


hash(45.56)


# In[66]:


ma_chaine = "Bonjour"
ma_chaine[0] = "C"


# In[67]:


ma_liste = [2,1,5,4]
ma_liste[0] = 15


# ## Boucles et conditions

# In[1]:


n1, n2, idx = 0, 1, 1
age, name = 36, "Justine"

while idx < 25:
    print(f"Bonjour {idx}. Je m'appelle {name}. J'ai {age} ans.")
    idx = 2*n2 + n1
    n2 = 2 * n1
    n1 += 1 
print("exterieur")


# In[6]:


liste_scores = [0.2, 0.1, .54, .76]

for score in liste_scores:
    print(score)
    
for i in range(len(liste_scores)):
    print(i)
    
for i in range(10):
    print("Bonjour")

for i in range(10, 20, 2):
    print(i)


# In[14]:


age = 19

if age < 18:
    print("Mineur")
elif age > 18:
    print("Majeur")
else:
    print("Va passer ton permis")


# In[ ]:


age = 19

if age > 18:
    print("Etape 1")
if age > 40:
    print("Etape 2")


# In[ ]:


age = 19

if age > 18:
    print("Etape 1")
elif age > 40:
    print("Etape 2")


# ## FizzBuzz
# 
# Pour tous les entiers de 0 à 100
# * Si l'entier est un multiple de 3 on affiche fizz
# * Si l'entier est un multiple de 5 on affiche buzz
# * Si l'entier est un multiple de 3 et 5 on affiche bazz
# * Sinon on affiche l'entier
# 

# In[20]:


for i in range(100):
    if (i % 3 == 0) and (i % 5 == 0):
        print("bazz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)


# In[9]:


from random import randint


valeur_secrete = randint(0,100)
proposition = int(input("Faites une proposition."))

while proposition != valeur_secrete:
    if proposition > valeur_secrete:
        print("La proposition est trop grande")
    else:
        print("la proposition est trop petite")
    proposition = int(input("Faites une proposition."))

print("Gagné")


# In[4]:


from random import randint


borne_min = 0
borne_max = 101
reponse = None

while reponse != "E":
    proposition = randint(borne_min+1, borne_max-1)#(borne_min + borne_max) // 2
    reponse = input(f"L'ordi  propose {proposition}. E/G/P ?")
    if reponse == "G":
        borne_min = proposition
    elif reponse == "P":
        borne_max = proposition
print("Gagné")


# In[7]:


from timeit import timeit
import numpy as np

get_ipython().run_line_magic('timeit', 'np.ones((20,10000))+2')


# In[8]:


def add():
    res = []
    for i in range(20):
        line = []
        for j in range(10000):
            line.append(1+2)
        res.append(line)

get_ipython().run_line_magic('timeit', 'add()')
            


# In[ ]:




