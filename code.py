import sys
import threading 
from threading import*
import time

d={} 


def create(key,name,phno,timeout=0):
    if key not in d:
            if len(d)<(1024*1020*1024) and sys.getsizeof(name)+sys.getsizeof(phno)<=(16*1024*1024): 
                if timeout==0:
                    l=[name,phno,timeout]
                else:
                    l=[name,phno,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
                    print("successfully created")
            else:
                print("error: Memory limit exceeded!! ")
        
    else:
      print("error: this key already exists") 
        

def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[2]!=0:
            if time.time()<b[2]: 
                stri="{"+"name"+":"+str(b[0])+","+"phno"+":"+str(b[1])+"}"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri="{"+"name"+":"+str(b[0])+","+"phno"+":"+str(b[1])+"}"
            return stri



def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[2]!=0:
            if time.time()<b[2]: 
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key is successfully deleted")
