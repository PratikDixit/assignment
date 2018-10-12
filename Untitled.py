
# coding: utf-8

# In[1]:


from  nsepy import get_history


# In[3]:


from datetime import date


# In[3]:


tcs=get_history(symbol="TCS",start=date(2015,1,1),
              end=date(2015,12,31))
tcs.to_csv("tcs.csv")


# In[4]:


nifty=get_history(symbol="NIFTY IT",start=date(2015,1,1),
                end=date(2015,12,31),index=True)
nifty.to_csv("nifty.csv")


# In[5]:


infy=get_history(symbol="INFY",start=date(2015,1,1),
                end=date(2015,12,31))
infy.to_csv("infy.csv")


# In[6]:


data=[tcs,infy,nifty]


# In[ ]:





# In[4]:


#ques first and second 
#one think  manage holiday
import  datetime
import pandas as pd
import matplotlib.pyplot as plt
def fun(date):
    df=pd.read_csv("tcs.csv",parse_dates=["Date"],index_col="Date")
    df1=pd.read_csv("nifty.csv",parse_dates=["Date"],index_col="Date")
    df2=pd.read_csv("infy.csv",parse_dates=["Date"],index_col="Date")    
    data=[df,df1,df2]
    data_name=["TCS","NIFTY","INFY"]
    color=["red","green","blue"]
    my_data=[]
    x=datetime.date(2015,1,1)
    for j in range(len(data_name)):
        my_data=data[j].Close.rolling(window=10).mean()
        my_data1=data[j].Close.dropna().mean()
        plt.plot(my_data,label=data_name[j])
      
        print("given data after droping NaN value=",my_data1)
        print("data for %s="%data_name[j])
        for i in date:
                  d1=datetime.timedelta(days=i*7)
                  d2=datetime.timedelta(days=(i+1)*7)
                  t1=x+d1
                  t2=x+d2
                  t1=str(t1)
                  t2=str(t2)
                  print("week %d ="%i,data[j][t1:t2].Close.mean())
            
       
              
date=[4,16,28,40,52] 
fun(date)

    


# In[5]:


#dummy time series
#all implementation only for tcs  
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
usb=CustomBusinessDay(calendar=USFederalHolidayCalendar())
print(usb)
df9=pd.read_csv("tcs.csv",parse_dates=["Date"],index_col="Date")
print(df9.Volume.head(5))


# In[6]:


#ques 3.1
#all implementation only for tcs 
row,col=df9.shape

(df9.Volume/(df9.Volume.shift()))*100>10
    


# In[7]:


#ques 3.2
#all implementation only for tcs 
df9.Close.shift()-df9.Close>2


# In[8]:


#plot tcs Closing2.2&2.1
#all implementation only for tcs 
rolling=df9.Close.rolling(window=10).mean().plot(label="avg")

close=plt.plot(df9.Close,label="Closing")
plt.legend(loc="upper right")
plt.show(block=False)


# In[9]:


#plt tcs volumn2.3
#all implementation only for tcs 
vlo=plt.plot(df9.Volume,color="red",label="Volume")
plt.legend(loc="upper right")
plt.show(block=False)

