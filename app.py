from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('crop_recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define seed URLs for different crops (replace with actual URLs)
seed_urls = {
    'rice': ['https://www.amazon.in/s?k=rice+seeds',
             'https://panseeds.in/product-category/improved-rice/'],
    'maize': ['https://www.iffcobazar.in/en/crops/maize/maize-seeds',
              'https://www.example.com/maize-seeds-2'],
    'chickpea': ['https://www.indiamart.com/proddetail/chickpea-seed-21548164673.html/',
                 'https://www.example.com/chickpea-seeds-2'],
    'kidneybeans': ['https://www.etsy.com/in-en/market/kidney_bean_seeds',
                    'https://www.amazon.in/s?k=kidney+beans&crid=2BJN2E37ABL01&sprefix=kidney%2Caps%2C564&ref=nb_sb_ss_ts-doa-p_1_6'],
    'pigeonpeas': ['https://www.badikheti.com/pigeon-pea-seeds',
                   'https://www.amazon.in/s?k=Pigeonpeas&crid=2O5KAZGZT1Q5F&sprefix=pigeonpeas%2Caps%2C329&ref=nb_sb_noss_2'],
    'mothbeans': ['https://www.indiamart.com/proddetail/moth-bean-seeds-23592925273.html/',
                  'https://www.amazon.in/s?k=moth+beans&crid=3MIN70T8NV274&sprefix=Mothbeans%2Caps%2C315&ref=nb_sb_ss_ts-doa-p_1_9'],
    'mungbean': ['https://www.ubuy.co.in/product/2ABYPU8M-handy-pantry-lihp-mng-mung-bean-sprouting-seed-8-oz',
                 'https://www.example.com/mungbean-seeds-2'],
    'blackgram': ['https://www.badikheti.com/black-gram-seeds',
                  'https://www.example.com/blackgram-seeds-2'],
    'lentil': ['https://www.exportersindia.com/indian-suppliers/lentil-seed.html/',
               'https://www.example.com/lentil-seeds-2'],
    'pomegranate': ['https://www.etsy.com/in-en/market/pomegranate_seeds',
                    'https://www.amazon.in/s?k=pomegranate+seeds&crid=NQ5D8M1VBIM0&sprefix=Pomegranate%2Caps%2C361&ref=nb_sb_ss_ts-doa-p_2_11'],
    'banana': ['https://www.amazon.in/Banana-Fruit-Plant/dp/B08JPGPCVR',
               'https://www.example.com/banana-seeds-2'],
    'mango': ['https://www.amazon.in/Mango-Fruit-Seeds/dp/B08JPGPCVR',
              'https://www.example.com/mango-seeds-2'],
    'grapes': ['https://www.amazon.in/dp/B08JPGPCVR?tag=bgms-21&ascsubtag=bing_6661e7ef9132c',
               'https://www.example.com/grapes-seeds-2'],
    'watermelon': ['https://www.bighaat.com/products/afa-306-watermelon?pf=search',
                   'https://www.example.com/watermelon-seeds-2'],
    'muskmelon': ['https://www.bighaat.com/products/ns-910-musk-melon?pf=search',
                  'https://www.example.com/muskmelon-seeds-2'],
    'apple': ['https://www.amazon.in/Apple-Fruit-Plant/dp/B08JPGPCVR',
              'https://www.example.com/apple-seeds-2'],
    'orange': ['https://nurserylive.com/products/orange-santra-seeds',
               'https://www.example.com/orange-seeds-2'],
    'papaya': ['https://www.bighaat.com/products/iris-hybrid-fruit-seeds-papaya-red-lady?pf=papayaSeeds',
               'https://www.example.com/papaya-seeds-2'],
    'coconut': ['https://www.amazon.in/Coconut-Plant/dp/B08JPGPCVR',
                'https://www.example.com/coconut-seeds-2'],
    'cotton': ['https://agribegri.com/products/nagraj-bgii-cotton-seeds--buy-online-cotton-seeds-.php',
               'https://www.example.com/cotton-seeds-2'],
    'jute': ['https://www.amazon.in/dp/B0BDM257R5?tag=bgms-21&ascsubtag=bing_6661f297d9c',
             'https://www.example.com/jute-seeds-2'],
    'coffee': ['https://www.amazon.in/dp/B09BRFTJDJ?tag=bgms-21&ascsubtag=bing_6661f3f022b',
               'https://www.example.com/coffee-seeds-2']
}

def predict_crop(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return prediction[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            nitrogen = float(request.form['nitrogen'])
            phosphorous = float(request.form['phosphorous'])
            potassium = float(request.form['potassium'])
            temperature = float(request.form['temperature'])
            ph = float(request.form['ph'])
            humidity = float(request.form['humidity'])

            features = [nitrogen, phosphorous, potassium, temperature, ph, humidity]
            label = predict_crop(features)
            seeds_urls = seed_urls.get(label, ["#", "#"])

            return render_template('index.html', label=label, seeds_urls=seeds_urls)
        except Exception as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
