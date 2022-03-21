from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [
    {
        "contact":"9876543210",
        "Name":"Rajesh",
        "done":False,
        "id":1
    },
    {
       "contact":"0123456789",
        "Name":"Ramesh",
        "done":False,
        "id":2  
    }
]

@app.route("/add-data",methods=["POST"])
def add_data() :
    if(not request.json):
        return jsonify({
            "status":"error",
            "message":"Please provide the data",
        },400)

    contact={
        "contact":request.json.get("contact",""),
        "Name":request.json("Name"),
        "done":False,
        "id":contacts[-1]["id"]+1
    }

    contacts.append(contact)
    return jsonify(
        {
            "status":"success",
            "message":"Contact added Successfully"
        }
    )

@app.route("/get-data")
def get_data() :
    return jsonify(
        {
            "data":contacts
        }
    )

if __name__ == "__main__":
    app.run(debug=True)