import pandas as pd
import datetime
import numpy as np
import streamlit
import xgboost as xgb

def main():
    html_temp="""
    <div style ="background-color:pink; padding:10px; ">
    <h2 style="color:black;text-align:center;"> Car Price Prediction Using ML</h2>
    
    </div>
    """
    model = xgb.XGBRegressor()
    model.load_model('xgb_model.json')
    streamlit.markdown(html_temp,unsafe_allow_html=True)

    streamlit.write('')
    streamlit.write('')
    streamlit.markdown("##### Are You Planning to sell your car ?\n###### So let's try to evaluating the price")

    p1 = streamlit.number_input("What is the current ex-showroom price of the Car (In Lakhs)",2.5,25.0,step=1.0)
    p2 = streamlit.number_input("What is the distance covered  by the car in kilometers?",100,50000000,step=200)
    s1 = streamlit.selectbox("What is the fuel type of the car?",('Petrol','Diesel','CNG'))

    if s1 == 'Petrol':
        p3=0
    elif s1 == 'Diesel':
        p3=1
    elif s1 == 'CNG':
        p3=2
    s2 = streamlit.selectbox("Are U a Dealer or Individual?", ('Dealer', 'Individual'))

    if s2 == 'Dealer':
        p4=0
    elif s2 == 'Individual':
        p4=1

    s3 = streamlit.selectbox("What is the transmission type?", ('Automatic', 'Manual'))

    if s3 == 'Manual':
        p5=0
    elif s3 == 'Automatic':
        p5=1


    p6 = streamlit.slider("number of Owners the car previously had?",0,3)

    date_time = datetime.datetime.now()

    years = streamlit.number_input("In which year car was purchased", 1990,date_time.year)
    p7 = date_time.year - years

    data_new = pd.DataFrame({
        'Present_Price': p1,
        'Kms_Driven': p2,
        'Fuel_Type': p3,
        'Seller_Type': p4,
        'Transmission': p5,
        'Owner': p6,
        'Age': p7
    }, index=[0])

    try:
        if streamlit.button('Predict'):
            pred = model.predict(data_new)
            if pred >0:
                streamlit.balloons()
                streamlit.success("now you can sell your car for {:.2f} lakhs".format(pred[0]))
            else:
                streamlit.warning("You can't able to sell this car")
    except:
        streamlit.warning("Something Went Wrong please try again")







if __name__ == '__main__':
    main()