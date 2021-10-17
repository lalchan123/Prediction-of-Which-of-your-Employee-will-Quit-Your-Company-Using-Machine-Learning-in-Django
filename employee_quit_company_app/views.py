from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from .models import EmployeeQuit
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")    

def result(request):  
    hr_df=pd.read_csv(r'F:\Project and Thesis\Project\Django Project\ML Django Project\Prediction of Which of your Employee will Quit Your Company\Employee_Quit_Company\hr_data.csv')
    s_df=pd.read_excel(r'F:\Project and Thesis\Project\Django Project\ML Django Project\Prediction of Which of your Employee will Quit Your Company\Employee_Quit_Company\employee_satisfaction_evaluation.xlsx')
    main_df= hr_df.set_index('employee_id').join(s_df.set_index('EMPLOYEE #'))
    main_df=main_df.reset_index()
    main_df.fillna(main_df.mean(),inplace=True)
    main_df.drop(columns='employee_id',inplace=True)
    le=LabelEncoder()
    main_df['salary']=le.fit_transform(main_df['salary'])
    main_df['department']=le.fit_transform(main_df['department'])
    X=main_df.drop(['left'],axis=1)
    y = main_df.left
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=89)
    model = LGBMClassifier(learning_rate=0.03,n_estimators=1000)
    model.fit(X_train,y_train)
    if request.method == "POST":
        n1 = float(request.POST['n1'])
        n2 = float(request.POST['n2'])
        n3 = float(request.POST['n3'])
        n4 = float(request.POST['n4'])
        n5 = float(request.POST['n5'])
        n6 = float(request.POST['n6'])
        n7 = float(request.POST['n7'])
        n8 = float(request.POST['n8'])
        n9 = float(request.POST['n9'])
        
        pred = model.predict(np.array([n1,n2,n3,n4,n5,n6,n7,n8,n9]).reshape(1,-1))
        result = ""
        if pred == [1]:
            result = "Employee will Leave"
        else:
            result = "Employee will stay"
        
        data = EmployeeQuit(number_project=n1,average_montly_hours=n2,time_spend_company=n3,Work_accident=n4,promotion_last_5years=n5,department=n6,salary=n7,satisfaction_level=n8,last_evaluation=n9,left=result)
        data.save()
    
    return render(request, "predict.html",{"result":result,})

def recordData(request):
    data = EmployeeQuit.objects.all().order_by('-id')
    paginator = Paginator(data, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "recordData.html",{"page_obj":page_obj, })  
