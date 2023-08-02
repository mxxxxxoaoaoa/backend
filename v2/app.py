from flask import Flask, jsonify
import database
db = database.Database()

app = Flask(__name__)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    res = db.get_all_posts()
    return jsonify(res)

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'class': '123'})


if __name__ == '__main__':
    app.run(debug=True)