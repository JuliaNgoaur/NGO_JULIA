#!/usr/bin/env python
# coding: utf-8

# In[23]:


def savings(gross_pay, tax_rate, expenses):

    after_tax_pay = int(gross_pay*(1 - tax_rate))
    take_home_pay = after_tax_pay - expenses

    return take_home_pay


# In[25]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    
    total_material_consumption = num_jobs * job_consumption
    waste = total_material - total_material_consumption
    
    return str(waste) + material_units


# In[ ]:


def interest(principal, rate, periods):
    
    interest = principal + (principal * (rate * periods))
    
    return int(interest)
    

