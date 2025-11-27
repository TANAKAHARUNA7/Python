from flask import Flask, request, make_response, jsonify

app = Flask(
    __name__,
    static_folder="resources/",
    static_url_path="/contents")

# print(f"app.static_folder: {app.static_folder}")
# print(f"app.static_url_path: {app.static_url_path}")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"name": "haruna", "age": 29})

@app.after_request
def post_process(response):
    return response

if __name__ == "__main__":
    app.run(debug=True)