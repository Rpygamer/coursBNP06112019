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


# In[ ]:


# Exercice

ma_liste = [True, None, 4, 6, 32, 7, 13, 12, [15, 16]]

# Récupérer le premier element
# Récupérer dernier élément
# Récupérer le premier element de la liste [15, 16] (à la fin)
# Récupérer un élément sur deux
# Récupérer du 2e au 6e inclus
# Récupérer du 2e à la fin de 2 en 2
# Récupérer de l'avant dernier au troisième




