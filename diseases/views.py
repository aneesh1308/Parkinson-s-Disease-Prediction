import pickle

from django.shortcuts import render
import cv2
import numpy as np
import keras
import os
from django.core.files.storage import FileSystemStorage
import re




def index(request):
    return render(request, 'disease/index.html', {})



def voice(request):
    if request.POST:

        val1 = request.POST.get('a')
        val2 = request.POST.get('b')
        val3 = request.POST.get('c')
        val4 = request.POST.get('d')
        val5 = request.POST.get('e')
        val6 = request.POST.get('f')
        val7 = request.POST.get('g')
        val8 = request.POST.get('h')
        val9 = request.POST.get('k')
        val10 = request.POST.get('l')
        val11 = request.POST.get('m')
        val12 = request.POST.get('n')
        val13 = request.POST.get('o')
        val14 = request.POST.get('p')
        val15 = request.POST.get('q')
        val16 = request.POST.get('r')
        val17 = request.POST.get('s')
        val18 = request.POST.get('t')
        val19 = request.POST.get('u')
        val20 = request.POST.get('v')
        val21 = request.POST.get('w')
        val22 = request.POST.get('x')

        str = [val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21,val22]

        float_features = []
        for x in str:
            float_features.append(float(x))
        features = [np.array(float_features)]
        pred = voicePrediction(features)

        context = {'pred': pred}
        return render(request, 'disease/voice.html', context)
    return render(request, 'disease/voice.html')



def spiral(request):
    media = 'media'
    if request.method == "POST" and request.FILES.get('upload'):
        if 'upload' not in request.FILES:
            err = 'NO image Selected'
            return render(request, 'disease/spiral.html', {"err": err})
        if request.FILES['upload'] == " ":
            err = 'No File Selected'
            return render(request, 'disease/spiral.html', {"err": err})
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        prediction = spiralprediction(os.path.join(media, file))
        context = {"pred": prediction, 'file_url': file_url}

        return render(request, 'disease/spiral.html', context)

    else:
        return render(request, 'disease/spiral.html')

def mriForm(request):
    media = 'media'
    if request.method == "POST" and request.FILES.get('upload'):
        if 'upload' not in request.FILES:
            err = 'NO image Selected'
            return render(request, 'disease/mriForm.html', {"err": err})
        if request.FILES['upload'] == " ":
            err = 'No File Selected'
            return render(request, 'disease/mriForm.html', {"err": err})
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        prediction = mriPrediction(os.path.join(media, file))
        context = {"pred": prediction, 'file_url': file_url}

        return render(request, 'disease/mriForm.html', context)

    else:
        return render(request, 'disease/mriForm.html')


def mriPrediction(path):
    model = keras.models.load_model('parkinson final stage classifier_95.h5')
    image = cv2.imread(path)
    image = cv2.resize(image, (512, 512))
    # image = np.expand_dims(image, axis=0)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    # image = cv2.resize(image,(500, 500))
    image = image.reshape(1, 512, 512, 3)
    prd = model.predict(image)
    prd = np.argmax(prd, axis=1)[0]

    # Make a prediction on the image
    # prediction = model.predict(image)

    # Print the prediction
    if prd == 1:
        pred = 'Parkinson\'s disease'
    elif prd == 0:
        pred = 'Healthy control'
    return pred


def voicePrediction(features):
    model =  pickle.load(open('model.pkl','rb'))
    prediction = model.predict(features)

    if prediction == 0:
        prediction = 'Heathly'
    else:
        prediction = "Parkinson's Disease"
    return prediction

def spiralprediction(path):
    model = keras.models.load_model('drawing pd.h5')
    image = cv2.imread(path)
    image = cv2.resize(image, (500, 500))
    # image = np.expand_dims(image, axis=0)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    # image = cv2.resize(image,(500, 500))
    image = image.reshape(1, 500, 500, 3)
    prd = model.predict(image)
    prd = np.argmax(prd, axis=1)[0]

    if prd == 1:
        pred = 'Parkinson\'s disease'
    elif prd == 0:
        pred = 'Healthy control'
    return pred