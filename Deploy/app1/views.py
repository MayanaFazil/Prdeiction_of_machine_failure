from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, models
from . forms import CreateUserForm, UserPredictDataForm
from django.contrib import messages
from . models import UserPredictModel
import joblib
import numpy as np

Model = joblib.load('G:/2023-2024/PROJECTS FOR 2023-2024/MACHINE LEARNING/ITPML04 - MACHINE FAILURE/Deploy/app1/model1.pkl')


def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, '2_register.html', context)


def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_login.html', context)

def logoutusers(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, '4_home.html')

def landingpage(request):
    return render(request, '1_landingpage.html')

def problem_statement(request):
    return render(request, '5_problem_statement.html')


# def model(request):
#     if request.method == 'POST':
#         fieldss = ['Air_temperature_K', 'Process_temperature_K', 'Rotational_speed_rpm', 'Torque_Nm', 'Tool_wear_min', 'Failure_Type']
#         form = UserPredictDataForm(request.POST)
#         features = []
#         try:
#             for i in fieldss:
#                 info = float(request.POST[i])  # Convert to float
#                 features.append(info)
            
#             Final_features = [np.array(features)]
#             alt_final_features = [np.array(Final_features)]
#             prediction = Model.predict(alt_final_features)
#             actual_output = prediction[0]
            
#             # Your code for mapping actual_output to failure types goes here...
            
#             if form.is_valid():
#                 print('Saving data in Form')
#                 form.save()
            
#             data = UserPredictModel.objects.latest('id')
#             data.Failure_Type = actual_output
#             data.save()
            
#             return render(request, 'model.html', {'form': form, 'prediction_text': actual_output})
        
#         except (KeyError, ValueError) as e:
#             # Handle invalid input or conversion errors here
#             error_message = f"Error: {str(e)}"
#             return render(request, 'model.html', {'form': form, 'error_message': error_message})

#     else:
#         print('Else working')
#         form = UserPredictDataForm(request.POST)
    
#     return render(request, 'model.html', {'form': form})


def model(request):
    if request.method == 'POST':
        fieldss = ['Air_temperature_K', 'Process_temperature_K', 'Rotational_speed_rpm', 'Torque_Nm', 'Tool_wear_min']
        form = UserPredictDataForm(request.POST)
        
        features = []
        for i in fieldss:
            info = float(request.POST[i])
            features.append(info)
           
        Final_features = [np.array(features, dtype=float)]
        
        prediction = Model.predict(Final_features)
        actual_output = prediction[0]
        print(actual_output)

        if actual_output == 0:
            actual_output = 'Heat Dissipation Failure'
            #return render(request, 'output.html', {'form':form,'prediction_text': actual_output})
        elif actual_output == 1:
            actual_output = 'No Failure'
            #return render(request, 'output.html', {'form':form,'prediction_text': actual_output})
        elif actual_output == 2:
            actual_output = 'Overstrain Failure'
            #return render(request, 'output.html', {'form':form, 'prediction_text': actual_output})
        elif actual_output == 3:
            actual_output = 'Power Failure'
            #return render(request, 'output.html', {'form':form, 'prediction_text': actual_output})
        elif actual_output == 4:
            actual_output = 'Random Failures'
            #return render(request, 'output.html', {'form':form, 'prediction_text': actual_output})
        elif actual_output == 5:
            actual_output = 'Tool Wear Failure'
            #return render(request, 'output.html', {'form':form, 'prediction_text': actual_output})
       
        
        print(features)
        print(actual_output)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
        data = UserPredictModel.objects.latest('id')
        data.Failure_Type = actual_output
        data.save()
        return render(request, 'output.html', {'form':form, 'prediction_text':actual_output})
    else:
        print('Else working')
        form = UserPredictDataForm(request.POST)    
    return render(request, 'model.html', {'form':form})

def model_database(request):
    models = UserPredictModel.objects.all()
    return render(request, 'model_database.html', {'models':models})
    
