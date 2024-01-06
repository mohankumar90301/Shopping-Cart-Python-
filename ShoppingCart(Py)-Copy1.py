#!/usr/bin/env python
# coding: utf-8

# In[1]:


class shop_cart():

 def __init__ (self):
    self.item_list=[]
    
 def add_item(self,name,price):#,qut,price
    items=(name,price)#,qut,price
    self.item_list.append(items)
    
 def remove_item(self,item_name):
     for i in self.item_list:
         if(i[0]==item_name):
            self.item_list.remove(i)
 def getTotal(self):
        total = 0
        for item in self.item_list:
            name, price = item # or price = item[1]
            total = total + price
            
# def quantity(self):
#     total_item=0
#     for i in range(self.item_list):
#         total_item=self.item_list+i
#         return total_item
 def getTotal(self):
        total = 0
        for item in self.item_list:
            price = item[1] # here item[1] inside bracket 1 means the second element u need to mentioned becoz item refers to int
                         #OR
            #name,price=item#here item refers to int
            total = total + price
        return total
         
cal=shop_cart()
    
cal.add_item("papaya",29)
cal.add_item("apple",20)
cal.add_item("papay",30)
#print("%i" %(cal.quantity()))
print(cal.item_list[0:])

cal.remove_item("apple")
print(cal.item_list[0:])
print(cal.getTotal())



# In[ ]:




