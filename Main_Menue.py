import Squeezer
import k_prototype

print ('" ---------Select one of the algorithms -------" ')
print (" 1) Kprototype algorithm ")
print (" 2) d-Squeezer  algorithm ")
option  = input("Enter option number  ")
print (" ---------Select data set to cluster   -------")
print (" 1) Credit Approval dataset ")
print (" 2) Heart Diseas dataset  ")
dataset= input (" Enter  dataset number ")
if (option ==1):
    k_prototype.k_prototype(dataset)
elif (option ==2):
    Squeezer.squeezer(dataset)
else:
    print("wrong option ")


