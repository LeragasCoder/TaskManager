from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline_days']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title...',
                'maxlength': 200
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description...',
                'rows': 4
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),
            'deadline_days': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of days until deadline',
                'min': 1
            })
        }
        labels = {
            'title': 'Task Title',
            'description': 'Description',
            'priority': 'Priority Level',
            'deadline_days': 'Deadline (Days)'
        }
    
    def clean_deadline_days(self):
        deadline_days = self.cleaned_data.get('deadline_days')
        if deadline_days and deadline_days < 1:
            raise forms.ValidationError('Deadline must be at least 1 day.')
        return deadline_days 