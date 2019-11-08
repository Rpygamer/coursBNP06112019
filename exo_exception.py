#!/usr/bin/env python
# coding: utf-8

# In[2]:


def addition(a, b):
    return a + b

print("debut")
addition(4, "bonjour")
print("fin")


# In[4]:


def division(a, b):
    return a / b

print("debut")
division(4, 0)
print("fin")


# In[22]:


import traceback


try:
    print("debut")
    assert 2 == 4, "erreur débile"
    addition(3, "bonjour")
    division(4, 0)
    print("fin")
except TypeError as e:
    traceback.print_exc()
    print("une type error", e)
except ZeroDivisionError as e:
    traceback.print_exc()
    print("une division par zero", e)
except Exception as e:
    traceback.print_exc()
    print("une erreur s'est produite", e)
print("terminer")


# In[27]:


class NotEnoughMoneyException(Exception):
    pass


try:
    un_compte = 1000
    for i in range(10):
        un_compte -= 200
        print(un_compte)
        if un_compte < 0:
            raise NotEnoughMoneyException()
except NotEnoughMoneyException as e:
    print("pas assez d'argent")
except Exception:
    print("erreur")

print("on continue")


# In[ ]:





# In[ ]:




