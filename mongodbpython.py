#!/usr/bin/python3
import pymongo
import re

#link to database and the specific set
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["miniproject3"]
mycol = mydb["information"]

#see whole set
x = mycol.find()
print('The whole set is:')
print(list(x))
print('\n')

#search for certain words
word={'keyword':'Food'}
print('Information where keyword=food:')
for x in mycol.find(word):
    print(x)
print('\n')

#see number of images per feed
sum=0
times=0
for x in mycol.find({},{'_id':0,'number_of_pictures':1}):
    sum+=x['number_of_pictures']
    times+=1
print('The number of images per feed is:')
print(sum/times)
print('\n')

#see most popular descriptors
for x in mycol.find({},{'_id':0,'keyword':1}):
    print(x)

