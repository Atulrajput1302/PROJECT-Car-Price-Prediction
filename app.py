from flask import Flask, render_template, request
import pickle
import sklearn
import numpy
# basic imports


#creating flask app
app = Flask(__name__)


#loading the model
model = pickle.load( open('model.pkl', 'rb') )


#creating home page route
@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')



#creating the predict page route
@app.route('/predict',methods=["GET", "POST"] )
def predict():
    if request.method == 'POST':

        Year = int(request.form['Year'])
        age = 2020 - Year


        Present_Price = float(request.form['Present_Price'])


        Kms_Driven = int(request.form['Kms_Driven'])


        Owner = int(request.form['Owner'])


        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1



        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0




        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0



        #creating the model#
        #note: must be passed in same order as it was in the dataframe\\\ order of passing the features must match with the order of columns-features
        #must be passed as 2D array with order
#|ORDER| Present_Price-->Kms_Driven-->Owner-->age-->Fuel_Type_Diesel-->Fuel_Type_Petrol -->Seller_Type_Individual-->Transmission_Manual



        prediction=model.predict([[Present_Price, Kms_Driven, Owner, age, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual ]])




        #forming the output [rounding the prediction]
        #note --> prediction is returned as 2D array --> so we need the 0th index --->(prediction[0]
        output = round(prediction[0],2)


        #displaying the output:
        if output<0:
            return render_template('result.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('result.html',prediction_text="You Can Sell The Car at Rs {} lakhs".format(output))




#when the method POST is not satisfied home.html is rendered
    else:
        return render_template('home.html')



































    return render_template('contact.html')




if __name__ == '__main__':
    app.run(debug=True)
