## This program generates a random user id and sends it in json format
## for it to be saved in Firebase in the document of the user.
import mongo_read
from flask import Flask, request, redirect, jsonify
import random
from flask_pymongo import pymongo
# import html_gen
import datetime, time


# connection_to_mongo_atlas = "mongodb+srv://tech_closet:blog_api_try@cluster0.xcgis.mongodb.net/<blog_api>?retryWrites=true&w=majority"
try:
    connection_to_mongo_atlas = "mongodb+srv://tech_closet:blog_api_try@cluster0.3odja.mongodb.net/<user_track>?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_to_mongo_atlas)
    db = client.get_database('user_track')
    print(db)
    user_collection = pymongo.collection.Collection(db, 'user_collection')
    mm = db.last_id
    # dict_of_form = {"_id": 10000, "email_type":"gmail.com", "last_date": datetime.datetime.now(), "random_id":10000}
    # db.last_id.insert_one(dict_of_form)
    print('connection successful')
except:
    print('error occured')

# client = pymongo.MongoClient(connection_to_mongo_atlas)
# db = client.get_database('blog_api')
# print(db)
# user_collection = pymongo.collection.Collection(db, 'user_collection')
# mm = db.db.collection

def updating_database(r_no, email_type):
    curr_date = str(datetime.datetime.now())
    r = mm.replace_one({"_id": 10000},
    {
        "email_type": email_type,
        "last_date": curr_date,
        "random_id": r_no
    })
    print(r)

app = Flask(__name__)

common_email_list = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']

@app.route('/id/<email>')
def generating_user_id(email):
    id_no = random.randint(50000,10000000)
    for t in common_email_list:
        if email.find(t) != -1:
            print(t + " found")
            user_name = email.replace(t, '')
            updating_database(id_no,t)
            user_name = user_name + str(id_no)
            print(user_name)
            # return str(user_name)
            return jsonify({"user_id": user_name})
        else:
            print('no')
        return "hello"



@app.errorhandler(404)
def func_error(error):
    return "Error 404: Page not found"

if __name__ == '__main__':
    print(datetime.datetime.now())
    app.run()
