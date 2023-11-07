from django.shortcuts import render
from django.http import JsonResponse
from .utils import analyze_data
from datetime import date

def analyze_data_view(request):
    if request.method == 'POST':
        data_str = request.POST.get('data', '')  
        print("Data as string (comma-separated):", data_str)

        if "datetime.date" in data_str:
            data_str = ""  
        data_str = data_str.replace(",", ".")  
        data_list = data_str.split()  
        data_list = [x.rstrip('.') for x in data_list]  
        print("Data as list:", data_list)
        data = []
        for x in data_list:
            x = x.strip()
            if x.replace(".", "", 1).isdigit() or (x.startswith('-') and x[1:].replace(".", "", 1).isdigit()):
                data.append(float(x))
            elif "datetime.date" in x:
                data.append(None)
        results = analyze_data(data)  
        for key, value in results.items():
            if value is None:
                results[key] = 'None' 
        return JsonResponse(results)  
    return render(request, 'data_analysis/analyze_data.html')
