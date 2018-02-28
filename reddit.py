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

app = Flask(__name__)

connection = pymongo.MongoClient("homer.stuy.edu")
connection.drop_database('keY-taoI')
db = connection['keY-taoI']
collection = db['r/deepFried']

object = urllib2.urlopen("https://www.reddit.com/r/deepfried.json")
string = object.read()
d = json.loads(string)

# deleting it every time
collection.drop()
# cleaning it up so the upper layers are gone
for document in d['data']['children']:
    collection.insert(document['data'])


def below_score(threshold):
    listy = []
    output = collection.find({"score" : {'$lt' : threshold}})
    for i in output:
        pprint(i)
        listy.append(i)
    return listy

def above_score(threshold):
    listy = []
    output = collection.find({"score" : {'$gt' : threshold}})
    for i in output:
        pprint(i)
        listy.append(i)
    return listy

def below_ups(threshold):
    listy = []
    output = collection.find({"ups" : {'$lt' : threshold}})
    for i in output:
        pprint(i)
        listy.append(i)
    return listy

def above_ups(threshold):
    listy = []
    output = collection.find({"ups" : {'$gt' : threshold}})
    for i in output:
        pprint(i)
        listy.append(i)
    return listy

def below_comments(threshold):
    listy = []
    output = collection.find({"num_comments" : {'$lt' : threshold}})
    for i in output:
        pprint(i)
        listy.append(i)
    return listy

def above_comments(threshold):
    listy = []
    output = collection.find({"num_comments" : {'$gt' : threshold}})
    for i in output:
        pprint(i)
        listy.append(i)
    return listy

@app.route('/', methods = ['POST', 'GET'])
def root():
    return render_template("reddit.html", results = "dummy")

@app.route('/tada', methods = ['POST', 'GET'])
def tada():
    contentType = request.form.get('contentType')
    compare = request.form.get('compare')
    value = request.form['value']
    print contentType
    print compare
    print value
    
    result = ''
    if (contentType == "score"):
        if (compare == "greater"):
            result = above_score(int(value))
        else:
            result = below_score(int(value))
    elif (contentType == "ups"):
        if (compare == "greater"):
            result = above_ups(int(value))
        else:
            result = below_ups(value)
    else:
        if (compare == "greater"):
            result = above_comments(int(value))
        else:
            result = below_comments(int(value))

    return render_template("reddit.html", results = result)

if __name__ == "__main__":
    app.debug = True
    app.run()