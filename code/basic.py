from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'CoolSecretKey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/informations.html')
def info():
    return render_template('informations.html')

@app.route('/casovy_plan.html')
def casovy_plan():
    return render_template('casovy_plan.html')


@app.route('/ubytovani.html')
def ubytovani():
    return render_template('ubytovani.html')

@app.route('/prihlaska.html')
def prihlaska():
    return render_template('prihlaska.html')

if __name__ == '__main__':
    app.run(debug=True)