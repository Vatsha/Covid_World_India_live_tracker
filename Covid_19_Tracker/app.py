from flask import Flask,request,render_template
from covid import Covid
from covid_india import states

import pydantic
import requests

 
app = Flask(__name__)
 
@app.route('/')

def home():
     covid = Covid()
     country = "India"
     data = covid.get_status_by_country_name(country)
     return render_template('index.html',data=data,country=country)

def home():
    state='Andhra Pradesh'
    data = states.getdata(state)
    return render_template('indDex.html',data=data,state=state)   



@app.route('/country/',methods=["POST"])
def search_country():
    if request.method == 'POST':
        covid = Covid()
        country = request.form['name']
        data = covid.get_status_by_country_name(country)
        return render_template('index.html',data=data,country=country)


@app.route('/country/state/',methods=["POST"])
def search_state():
    if request.method == 'POST':
        state = request.form['state']
        data = states.getdata(state)
        return render_template('index.html',data=data,state=state)




if __name__== '__main__':
    app.run(debug=True)
