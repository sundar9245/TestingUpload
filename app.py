# Get the database using the method we defined in pymongo_test_insert file
import os
from python_get_db import get_database
from flask import Flask, render_template, request, url_for, redirect, jsonify

app = Flask(__name__)

dbname = get_database()

db = dbname.web_gallery_list
collection_name = db.web_items
port = int(os.environ.get('PORT', 5000)) 
#Search
item_details = collection_name.find({"category" : "Game"})
for item in item_details:
   # This does not give a very readable output
   print(item)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html', content=list(collection_name.find()))

@app.route('/Contact', methods=['GET'])
def Contact():
    return render_template('Contact.html')

@app.route('/About', methods=['GET'])
def About():
    return render_template('About.html')

@app.route('/Economics/', methods=['GET'])
def Economics():
    return render_template('Economic.html', content=list(collection_name.find({"category" : "Economic"})))
    
@app.route('/Education/', methods=['GET'])
def Education():
    return render_template('Education.html', content=list(collection_name.find({"category" : "Education"})))

@app.route('/Books/', methods=['GET'])
def Books():
    return render_template('Books.html', content=list(collection_name.find({"category" : "Books"})))

@app.route('/Games/', methods=['GET'])
def Games():
    return render_template('Games.html', content=list(collection_name.find({"category" : "Games"})))

@app.route('/Softwares/', methods=['GET'])
def Softwares():
    return render_template('softwares.html', content=list(collection_name.find({"category" : "Softwares"})))

@app.route('/Mobiles/', methods=['GET'])
def Mobiles():
    return render_template('Mobiles.html', content=list(collection_name.find({"category" : "Mobiles"})))

@app.route('/Shops/', methods=['GET'])
def Shops():
    return render_template('Shops.html', content=list(collection_name.find({"category" : "Shops"})))

@app.route('/Others/', methods=['GET'])
def Others():
    return render_template('Others.html', content=list(collection_name.find({"category" : "Others"})))

@app.route('/Tools', methods=['GET'])
def Tools():
    return render_template('Tools.html', content=list(collection_name.find({"category" : "Tools"})))

if '__name__' == "__main__":
    app.run(host='0.0.0.0', port=port)
