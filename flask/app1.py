# Flask ライブラリから Flask クラスだけを持ってくる。
# Flask クラスを元に「アプリ本体（サーバー）」を作る。
from flask import Flask, Response

print("__name__ の中身：", __name__)

#　app が Flask アプリの“本体”
app = Flask(__name__)

# どのルートでも共通で、リクエスト処理の前に呼ばれる関数を登録する
@app.before_request
def prt_log():
    print("log")
    
@app.route("/", methods=["GET"])
def home():
    print("log")
    # return "本文, ステータスコード, {ヘッダー辞書}"
    return "hello flask", 200, {"GSC" : "gsc"}

@app.route("/student/<int:id>", methods=["GET"])
def student(id):
    return f"Student ID : {id}"

@app.after_request
def prt_after(rsp:Response):
    print(rsp.headers.get('gsc'))
    return rsp
    
@app.teardown_request
def teardown(e:Exception):
    print(e)
       
if __name__ == "__main__":
    app.run(debug=True)
    
