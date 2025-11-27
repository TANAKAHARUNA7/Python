from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    # body = "Hello Flask"
    # resp = make_response(body, 200)
    # resp.headers['TEST 1'] = 1
    # resp.headers['TEST 2'] = 2
    # resp.headers['TEST 3'] = 3
    
    # print(request.headers.get("sort"))
    # print(request.headers.get("Content-Type"))
    # return "hello", 200, {"Test-Code" : "GSC"}
    # return resp
    return jsonify({"name": "haruna", "age": 29}, 200)

# return jsonify({"name": "haruna", "age": 29}, 200) 

@app.after_request
def post_process(response):
    return ...

if __name__ == "__main__":
    app.run(debug=True)