from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('rdt.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
	
	if request.method == 'POST':
		arrival_year = int(request.form['arrival_year'])
		arrival_date_day = int(request.form['arrival_date_day'])
		adults = int(request.form['adults'])



		meds_name_corex=request.form['meds_name_corex']
		if(meds_name_corex=='corex'):
			meds_name_corex=1
			meds_name_crocin=0
			meds_name_disprin=0
			meds_name_nizer=0
			meds_name_paracetamol=0
			meds_name_vibact=0
		elif(meds_name_corex=='crocin'):
			meds_name_corex=0
			meds_name_crocin=1
			meds_name_disprin=0
			meds_name_nizer=0
			meds_name_paracetamol=0
			meds_name_vibact=0
		elif(meds_name_corex=='disprin'):
			meds_name_corex=0
			meds_name_crocin=0
			meds_name_disprin=1
			meds_name_nizer=0
			meds_name_paracetamol=0
			meds_name_vibact=0		
		elif(meds_name_corex=='nizer'):
			meds_name_corex=0
			meds_name_crocin=0
			meds_name_disprin=0
			meds_name_nizer=1
			meds_name_paracetamol=0
			meds_name_vibact=0
		elif(meds_name_corex=='paracetamol'):
			meds_name_corex=0
			meds_name_crocin=0
			meds_name_disprin=0
			meds_name_nizer=0
			meds_name_paracetamol=1
			meds_name_vibact=0
		else:
			meds_name_corex=0
			meds_name_crocin=0
			meds_name_disprin=0
			meds_name_nizer=0
			meds_name_paracetamol=0
			meds_name_vibact=1


		market_segment_Online = request.form['market_segment_Online']
		if(market_segment_Online=='Online'):
			market_segment_Online=1
		else:
			market_segment_Online=0

		customer_type_Group = request.form['customer_type_Group']
		if(customer_type_Group=='Group'):
			customer_type_Group=1
			customer_type_Transient=0
		else:
			customer_type_Group=0
			customer_type_Transient=1		
					
		prediction=model.predict([[arrival_year,arrival_date_day,adults,meds_name_corex,meds_name_crocin,meds_name_disprin,meds_name_nizer,meds_name_paracetamol,meds_name_vibact,market_segment_Online,customer_type_Group,customer_type_Transient]])
		output=round(prediction[0],2)
		if output<0:
			return render_template('index.html',prediction_texts="Not enough input!!!")
		else:
			return render_template('index.html',prediction_text="{}".format(output))
	else:
		return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)	