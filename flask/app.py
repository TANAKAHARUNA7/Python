from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    print(f"Path: {request.path}")
    print(f"Method: {request.method}")
    # response
    return "hello flask", 200 , {"GSC" : "gsc"}

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)