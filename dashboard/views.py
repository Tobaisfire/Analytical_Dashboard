from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import FileUploadForm
import pandas as pd
from pivottablejs import pivot_ui
from IPython.lib.display import IFrame
from IPython.display import HTML

def analytic_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            filepath = file.file.path

            # Read the uploaded file using pandas
            
            if filepath.endswith('.csv'):
                df = pd.read_csv(filepath)
            elif filepath.endswith('.xlsx') or filepath.endswith('.xls'):
                df = pd.read_excel(filepath)

            # Perform data analysis and visualization using pandas or other libraries
            # Generate pivot tables, charts, or any other desired visualizations
            pivot_data = pivot_ui(df)
            

            with open(r'D:\keval\study\Projects\Django\Dashboard\analytic_dashboard\pivottablejs.html','r') as fp:
                store = fp.read()

            with open(r'dashboard\templates\dashboard.html','w') as f:
                f.write(store)

            return render(request,'dashboard.html')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})
