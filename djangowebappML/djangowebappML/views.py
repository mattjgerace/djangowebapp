from django.shortcuts import render
from django.template.context_processors import csrf
import os

# our home page view
def home(request):    
    return render(request, 'index.html')

# custom method for generating predictions
def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):
    import pickle
    path1 = os.path.join(os.path.dirname(__file__), "titanic_survival_ml_model.sav")
    path2 = os.path.join(os.path.dirname(__file__), "scaler.sav")
    model = pickle.load(open(path1, "rb"))
    scaled = pickle.load(open(path2, "rb"))
    prediction = model.predict(scaled.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]]))
    
    if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"
        

# our result page view
def result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    embQ = int(request.GET['embQ'])
    embS = int(request.GET['embS'])

    result = getPredictions(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)

    return render(request, 'result.html', {'result':result})