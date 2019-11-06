#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver

navigateur = webdriver.Chrome()


# In[6]:


navigateur.get("https://www.seloger.com/")


# In[7]:


search = navigateur.find_element_by_css_selector(".c-quest-actions-search")
search.click()


# In[8]:


liste_prix_html = navigateur.find_elements_by_css_selector(".jGOFou")


# In[12]:


liste_prix = []
for html_elm in liste_prix_html:
    liste_prix.append(int(html_elm.text.replace(" ", "").replace("€", "")))


# In[14]:


sum(liste_prix)/len(liste_prix)


# In[ ]:




