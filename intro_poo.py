#!/usr/bin/env python
# coding: utf-8

# In[25]:


from random import randint


class Person:
    def __init__(self, prenom, age_init=65, solde_init=10000):
        self.firstname = prenom
        self.age = age_init
        self.location = "Bordeaux"
        self.compte = Compte(solde_init)
      
    def say_hi(self):
        print(f"Bonjour, je m'appelle {self.firstname}.")
        
    def transfert(self, other, montant):
        self.compte.retrait(montant)
        other.compte.depot(montant)
        
    def __str__(self):
        return f"firstname = {self.firstname}"
    
    def __lt__(self, other):
        assert type(other) == Person, ("On ne peut pas comparer "
                                       "une personne et autre chose")
        return self.age < other.age

    def __eq__(self, other):
        assert type(other) == Person, ("On ne peut pas comparer "
                                       "une personne et autre chose")
        return self.age == other.age
    
    def __getitem__(self, index):
        return randint(0,10)


une_personne = Person("Martin", 6)
une_autre_personne = Person("Jeanne")

une_autre_personne.transfert(une_personne, 100)

print(une_personne.age)
print(une_autre_personne.age)

une_personne.firstname = "Mylenne"

print(une_personne.firstname)
print(une_autre_personne.firstname)

une_personne.say_hi()


# In[24]:


une_personne[0]


# In[12]:


print(une_personne)
print(type(une_personne))


# In[20]:


print(une_autre_personne.age)
print(une_personne.age)

une_autre_personne < une_personne
7 < une_personne
une_autre_personne < 4


# In[46]:


from random import randint
import traceback

class NotEnoughMoneyException(Exception):
    def __init__(self, compte, montant):
        self.compte = compte
        self.montant = montant
    def corriger(self):
        self.compte.depot(montant)

class Compte:
    def __init__(self, solde_init):
        self.solde = solde_init
    
    def retrait(self, montant):
        assert montant > 0, ("On ne peut pas retrirer "
                               "un montant négatif")
        assert montant < self.solde, "Solde insuffisant"
        self.solde -= montant
        print(f"solde restant : {self.solde}")
    
    def depot(self, montant):
        assert montant > 0, ("On ne peut pas déposer "
                               "un montant négatif")
        self.solde += montant
        print(f"solde restant : {self.solde}")

        
class CompteCheque(Compte):
    # rajouter decouvert_max en attribut (par défaut 500)
    def __init__(self, solde_init, decouvert_max=500):
        Compte.__init__(self, solde_init)
        self.decouvert_max = decouvert_max
        
    def retrait(self, montant):
        assert montant > 0, ("On ne peut pas retrirer "
                               "un montant négatif")
        self.solde -= montant
        if self.solde < -self.decouvert_max:
            raise NotEnoughMoneyException(self, montant)
            
        print(f"solde restant : {self.solde}")


class CompteEpargne(Compte):
    def __init__(self, solde_init, interet=1.02):
        Compte.__init__(self, solde_init)
        self.interet = interet

class Person:
    def __init__(self, prenom, age_init=65, solde_init=10000):
        self.firstname = prenom
        self.age = age_init
        self.location = "Bordeaux"
        self.compte = CompteCheque(solde_init)
        self.note = 100
      
    def say_hi(self):
        print(f"Bonjour, je m'appelle {self.firstname}.")
        
    def transfert(self, other, montant):
        assert type(other) == Person, ("On ne peut pas transfert "
                                       "à autre chose qu'une personne")
        try:
            self.compte.retrait(montant)
            other.compte.depot(montant)
        except AssertionError as e:
            print("Error", e)
            self.note -= 1
        except NotEnoughMoneyException as e:
            print("Error", e)
            e.corriger()
        
    def __str__(self):
        return f"firstname = {self.firstname}"
    
    def __lt__(self, other):
        assert (type(other) == Person) or                 (type(other) == int), ("On ne peut pas comparer "
                                       "une personne et autre chose")
        return self.age < other.age

    def __eq__(self, other):
        assert type(other) == Person, ("On ne peut pas comparer "
                                       "une personne et autre chose")
        return self.age == other.age
    
    def __getitem__(self, index):
        return randint(0,10)


une_personne = Person("Martin", 6)
une_autre_personne = Person("Jeanne")
try:
    une_personne.transfert(une_autre_personne, 5000000)
except AssertionError as e:
    print("une erreur est survenue", e)
except TypeError as e:
#     traceback.print_stack()
    print("une type erreur est survenue", e)
except NotEnoughMoneyException as e:
    print("une type erreur est survenue", e)
except:
    print("Une erreur inattendue est survenue")
    
print(une_personne.compte.solde)


# In[ ]:




