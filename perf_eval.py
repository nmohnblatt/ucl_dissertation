#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Variables

t = 6 #threshold of servers
N_users = 10**9 #number of registered users
N_contacts = 1 #number of contacts


# In[7]:


# Operation timings for mobile devices.
# Sources provided in comments.
# Times in milliseconds

# Mobile parameters
pair = 11.752 #https://github.com/herumi/mcl/blob/master/bench.txt
add0 = 0.015
add1 = 0.03
mul0 = 2.615
mul1 = 4.581
hash0 = 0.507
hash1 = 9.93

#Server parameters
PAIR = 7.353
MUL0 = 1.592
MUL1 = 2.955

#DSA parameters
dsas = 10**3/1212.33 #https://www.wolfssl.com/docs/benchmarks/
dsav = 10**3/331.02


# In[8]:


setup_u = t*(4*(mul0+mul1+pair)+add0+add1+dsas)
print("user needs ", setup_u, "ms to perform setup with ", t, "servers")


# In[11]:


setup_s =  N_users*(4*PAIR + MUL0 + MUL1 + dsav)
days = setup_s/10**3/60/60/24
print("server needs ", days, "days to enroll ", N_users, "users")


# In[10]:


key_u = N_contacts*(2*pair+hash0 + hash1)
print("user needs ", key_u, "ms to key derivation for ", N_contacts, "contacts")


# In[ ]:




