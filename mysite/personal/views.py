from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from personal.models import Contact
from joblib import load
import pandas as pd

model = load('./Saved_Models/model.joblib')

def index_view(request):
    template = loader.get_template('index.html')

    context = {}

    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return render(request, "contact_done.html")

    return HttpResponse(template.render(context, request))

def bmi_view(request):
    template = loader.get_template('bmi.html')
    context = {}

    if request.method == 'POST':
        Gender = request.POST['Gender']
        Height = float(request.POST['Height'])
        Weight = float(request.POST['Weight'])

        # Ensure the feature names match those used during model training
        columns = [ 'Height', 'Weight', 'Gender_Female', 'Gender_Male']
        data = {
            'Height': [Height],
            'Weight': [Weight],
            'Gender_Female': [1 if Gender == 'female' else 0],
            'Gender_Male': [1 if Gender == 'male' else 0]
        }

        # Create a DataFrame with the correct feature order
        input_df = pd.DataFrame(data, columns=columns)

        # Predict using the loaded model
        y_pred = model.predict(input_df)

        # Map predicted index to categories
        categories = ['Extremely Weak', 'Weak', 'Normal', 'Overweight', 'Obesity', 'Extremely Obesity']
        bmi_category = categories[y_pred[0]]

        return render(request, 'bmi.html', {'result': bmi_category})

    return HttpResponse(template.render(context, request))