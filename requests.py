#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# module 설치
get_ipython().system('pip install requests  ')


# In[1]:


# 모듈 import
import requests


# In[ ]:


# 네이버 메인 페이지 가져오기
URL = 'http://www.naver.com'
naverhome = requests.get(URL) 
print(naverhome.status_code)
print(naverhome.text)


# In[ ]:


# 구글 검색 페이지 이용, python 검색 결과 가져오기
URL = 'https://www.youtube.com/results'
myhome = {'search_query':'코딩'}
response = response.get(URL)
print(myhome.status_code)


# In[ ]:


print(response.text)


# In[9]:



URL = 'http://hwan9619.pythonanywhere.com/friends/'
parameters = {'search_query':'코딩'}
myhome = requests.get(URL)
print(response.status_code)
html_data = myhome.text


# In[3]:


print(response.text)


# In[18]:


html_data.find('NCTECH')


# In[20]:


print(html_data[2741:2747])


# In[ ]:




