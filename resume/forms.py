from django import forms

from .models import Resume

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('gender', 'tel', 'address', 'grade', 
		'上门时间', '家教要求', '孩子基本信息',)
