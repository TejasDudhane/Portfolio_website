from django.shortcuts import render
from testapp.forms import ContactDbForm

def contactview(request):
    if request.method == 'POST':
        form = ContactDbForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Record inserted into database successfully....')
    form = ContactDbForm()
    return render(request,'testapp/contact.html',{'form':form})
def messageview(request):
    return render(request,'testapp/message.html')
def home_page_view(request):
    return render(request,'testapp/home.html')
def about(request):
    return render(request,'testapp/about.html')
def summary(request):
    return render(request,'testapp/summary.html')
def skills(request):
    return render(request,'testapp/skills.html')
def experience(request):
    return render(request,'testapp/experience.html')
def education(request):
    return render(request,'testapp/education.html')
def project(request):
    return render(request,'testapp/project.html')
def certifications(request):
    return render(request,'testapp/certifications.html')
def personalinfo(request):
    return render(request,'testapp/pinfo.html')
def awards(request):
    return render(request,'testapp/awards.html')
def qualities(request):
    return render(request,'testapp/qualities.html')
def activities(request):
    return render(request,"testapp/activities.html")
