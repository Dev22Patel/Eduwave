from django.shortcuts import render, redirect
from .forms import CourseForm  # Make sure to import the EventForm
from django.contrib import messages  # Import messages framework to show success/error messages
from django.http import HttpResponse
from .models import Course
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The course has been added successfully!')
            return redirect('home')  
        else:
            print(form.errors)
            return HttpResponse("not registered")
    else:
        form = CourseForm()
        messages.success(request, 'The course has been added successfully!')

    return render(request, 'home.html', {'form': form})


def course_form(request):
    return render(request,"form.html")


# def serve_file(request, file_name):
#     # Retrieve the model instance using the file name
#     try:
#         instance = Course.objects.get(file_field=file_name)
#     except Course.DoesNotExist:
#         return HttpResponse("File not found", status=404)
    
#     # Retrieve the file content
#     file_content = instance.file_field.read()
    
#     # Determine the file's content type
#     content_type = 'application/octet-stream'  # Default content type
#     if instance.file_field.name.endswith('.pdf'):
#         content_type = 'application/pdf'
#     elif instance.file_field.name.endswith('.jpg'):
#         content_type = 'image/jpeg'
#     # Add more conditions for other file types as needed
    
#     # Create an HttpResponse object with the file content and appropriate content type
#     response = HttpResponse(file_content, content_type=content_type)
    
#     # Set the Content-Disposition header to force download or inline display
#     response['Content-Disposition'] = f'attachment; filename="{file_name}"'  # Force download
#     # response['Content-Disposition'] = f'inline; filename="{file_name}"'  # Inline display
    
#     return response