from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['CourseName', 'CoursePrice', 'CourseDuration', 'TeacherName', 'LastUpdated', 'Description']



