from django.shortcuts import render
from ResumeApiapp.models import Resumeapi
from ResumeApiapp.forms import ResumeapiForm

# Create your views here.
#creating add resume api views
def add_resume_view(request):
    form = ResumeapiForm()
    if request.method == 'POST':
        form = ResumeapiForm(request.POST)
        if form.is_valid():
            form =form.cleaned_data
            form.save()
    return render(request,'ResumeApiapp/addresume.html',{'form':form})
