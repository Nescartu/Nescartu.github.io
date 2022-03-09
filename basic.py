from flask import Flask, render_template
from form import InfoForm, NumberOfPersonsForm
from flask_frozen import Freezer


app = Flask(__name__)

app.config['SECRET_KEY'] = 'CoolSecretKey'

#app.config['MAIL_SERVER']='smtp.gmail.com'
#app.config['MAIL_PORT'] = 465
#app.config['MAIL_USERNAME'] = 'kubadrahotsky@gmail.com'
#app.config['MAIL_PASSWORD'] = 'egoqihzmnjlgfcdb'
#app.config['MAIL_USE_TLS'] = False
#app.config['MAIL_USE_SSL'] = True
#mail = Mail(app)
#formular_data = []
global pocet_osob

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/informations')
def info():
    return render_template('informations.html')

@app.route('/casovy_plan')
def casovy_plan():
    return render_template('casovy_plan.html')


@app.route('/okoli')
def okoli():
    return render_template('okoli.html')

@app.route('/prihlaska', methods=['GET', 'POST'])
def prihlaska():
    jmeno = False
    prijimeni = False
    #pocet_osob = False
    
    #form_number = NumberOfPersonsForm()
    #if form_number.validate_on_submit():
    #    pocet_osob = form_number.pocet_osob.data
        

    form = InfoForm()
    if form.validate_on_submit():
        jmeno = form.jmeno.data
        prijimeni = form.prijimeni.data
        
        #formular_data.append(jmeno)
        #formular_data.append(prijimeni)
        #mail_fuction(formular_data)

        form.jmeno.data = ''
        form.prijimeni.data = ''
        return render_template('index.html')

    return render_template('prihlaska.html', form = form, jmeno = jmeno, prijimeni = prijimeni)

#@app.route("/mail")
#def mail_fuction(formular_data):
#   msg = Message(formular_data[0] +" " + formular_data[1], sender = 'kubadrahotsky@gmail.com', recipients = ['kubadrahotsky@gmail.com'])
#   msg.body = "Svatba Tasov \n" + ''.join([str(elem)+"\n" for elem in formular_data])
#   mail.send(msg)
#   return "Sent"

def send_pocet_osob():
    return pocet_osob

if __name__ == '__main__':
    app.run(debug=True)