from flask import Flask, jsonify,request
app=Flask(__name__)
tasks=[
    {'ID':1,'Title':u'Buy Groceries','Description':u'Milk, Iced Tea, Bread','Done':False},
    {'ID':2,'Title':u'learnPython','Description':u'find good python tutorial','Done':False}
]
@app.route("/")
def hello_world():
    return "Hello World!"
@app.route("/add-task",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":
            "error","message":
            "pleaseProvidetheTask"
        },530453080)
    task={
        'ID':tasks[-1]['ID']+1,
        'Title':request.json["Title"],
        'Description':request.json.get('Description',""),
        'Done':False
    }
    tasks.append(task)
    return jsonify({
        "status":
        "succsess","Message":"Task Added Successfulliy"
    })
@app.route("/get-data")
def get_data():
    return jsonify({
        "data":tasks
    })
if(__name__=="__main__"):
    app.run(debug=True)