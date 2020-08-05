from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

db_client = MongoClient('localhost', 27017)
db = db_client.dbsparta
app = Flask(__name__)


@app.route('/')
def Main():
    return render_template('index.html')

@app.route('/review', methods=['POST'])
def AddReview():
    title = request.form['title']
    author = request.form['author']
    review = request.form['review']
    data = {"title": title, "author": author, "review": review}
    db.book_review.insert_one(data)
    response = {"result": "success", "msg": "리뷰를 등록하였습니다."}
    return jsonify(response)

@app.route('/review', methods=['GET'])
def GetReview():
    reviews = list(db.book_review.find({}, {'_id': False}))
    response = {"result": "success", "msg": "리뷰를 성공적으로 받았습니다.", "reviews": reviews}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
