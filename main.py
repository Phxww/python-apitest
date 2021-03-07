from flask import Flask, jsonify, request

app = Flask(__name__)

user_list = [
    {
        'username': 'abc',
        'password': 'abc',
    }, {
        'username': '123',
        'password': '123',
    }
]


@app.route('/')
def helloworld():
    return "hello world!!"


@app.route('/users', methods=['GET'])
def get_user():
    return jsonify(user_list)


@app.route('/user', methods=['POST'])
def create_user():
    user = request.get_json()
    user_check = list(
        filter(
            lambda x: user.get('username') == x['username'],
            user_list
        )
    )
    if not user_check:
        user_list.append(user)
        return jsonify({
            'message': 'user created'
        })
    else:
        return jsonify(
            {'message': 'user exist'}
        )


if __name__ == "__main__":
    app.run()
