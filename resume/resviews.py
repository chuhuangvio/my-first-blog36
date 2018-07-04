from django.shortcuts import render
from django.http import HttpRequest
from .forms import ResumeForm
from resume.models import Resume
from datetime import datetime
from django.http import Http404
from django.shortcuts import redirect

# Create your views here.
def resume_new(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.author = 'oldman'
            resume.date_time = datetime.now()
            resume.save()
            return redirect('detail', id = 6)
    else:
        form = ResumeForm()
    return render(request, 'resume_edit.html', {'form': form})

