from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form["name"]
    count = request.form["count"]
    address = request.form["address"]
    phone_num = request.form["phone_num"]

    insert_data = {"name": name, "count": count, "address": address, "phone_num": phone_num}
    print(insert_data)
    db.orders.insert_one(insert_data)

    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({}, {"_id": False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run()