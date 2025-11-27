from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    
    uploaded_file_name = None
    
    print(request.headers.get('gsc'))
    file_obj = request.files.get("file_1")
    if file_obj:
        uploaded_file_name = file_obj.filename
        
    return {
        "method" : request.method,
        "url"    : request.url,
        "path"   : request.path,
        "query"  : request.args,
        "form"   : request.form,
        "headers": dict(request.headers),
        "cookies":request.cookies,
        "files"  : uploaded_file_name,
        "json"   : request.get_json(silent=True),
        "remote_addr" : request.remote_addr        
    }

if __name__ == "__main__":
    app.run(debug=True)