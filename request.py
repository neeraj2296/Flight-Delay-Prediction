from flask import Flask, request

app = Flask(__name__)

@app.route('/query_example')
def query_example():
    lang = request.args.get('language')
    return '<h1> The language is : {}</h1>'.format(lang)



if __name__ == '__main__':
    app.run(debug=True)