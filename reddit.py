'''
/r/DeepFried json from reddit
it includes data about each post on the front page of the DeepFried at real time if you comment stuff in

https://www.reddit.com/r/deepfried.json

I got rid of several top layers so I could have separate documents for each post
I just established a connection in this script
'''

from flask import Flask, render_template, request
import pymongo
import json, urllib2
from pprint import pprint

connection = pymongo.MongoClient("homer.stuy.edu")
connection.drop_database('keY-taoI')
db = connection['keY-taoI']
collection = db['r/deepFried']

object = urllib2.urlopen("https://www.reddit.com/r/deepfried.json")
string = object.read()
d = json.loads(string)

collection.insert(d)

# deleting it every time
# db['r/deepFried'].drop()
# cleaning it up so the upper layers are gone
# for document in d['data']['children']:
#     collection.insert(document['data'])

def below_score(threshold):
    output = collection.find({"score" : {'$lt' : threshold}})
    for i in output:
   		pprint("hlweriewlr")

def above_score(threshold):
    output = collection.find({"score" : {'$gt' : threshold}})
    for i in output:
   		pprint(i)

def below_ups(threshold):
    output = collection.find({"ups" : {'$lt' : threshold}})
    for i in output:
   		pprint(i)

def above_ups(threshold):
    output = collection.find({"ups" : {'$gt' : threshold}})
    for i in output:
   		pprint(i)

def below_comments(threshold):
    output = collection.find({"num_comments" : {'$lt' : threshold}})
    for i in output:
   		pprint(i)

def above_comments(threshold):
    output = collection.find({"num_comments" : {'$gt' : threshold}})
    for i in output:
   		pprint(i)

def testingfxn():
    return("testingfunctionprinted")

def displayResults():
  return "<Display Results>"





   		

app=Flask(__name__)

@app.route('/')
def root():
    return render_template("reddit.html", results = displayResults())




if __name__ == "__main__":
    app.debug = True
    app.run()
