from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def head():
    first = 'bu benim ilk condition tecrübem'
    return render_template('index.html', message = first)

@app.route('/mert')
def mylist():
    names = ["ahmet arif", "salih", "tarkan", "sergio", "hadi abim evine", "bu kadar eğlence yeter"]
    return render_template('body.html', object = names)














if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=80)