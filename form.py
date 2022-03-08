from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
#from basic import send_pocet_osob


class InfoForm(FlaskForm):
   
    for i in range(5):
        jmeno = StringField("Jméno: " )
        prijimeni = StringField("Přijmení: " )
        
    submit = SubmitField('Odeslat')
    
class NumberOfPersonsForm(FlaskForm):
    pocet_osob = IntegerField("Kolik osob registrujete:")
    
    submit = SubmitField('Pokračovat')
    
