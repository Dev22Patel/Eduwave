from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
import uuid
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4 , editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class Course(BaseModel):
    CourseName = models.CharField(max_length=100)
    CoursePrice = models.DecimalField(max_digits=10, decimal_places=2)
    CourseDuration = models.CharField(max_length=100)
    TeacherName = models.CharField(max_length=100)
    file = models.FileField(null=True, blank=True,upload_to= 'course/')
    course_image = models.ImageField(null=True,blank=True,upload_to= 'course_photo/')
    LastUpdated = models.DateField()
    Description = models.TextField()
    
    def __str__(self):
        return self.CourseName


class Cart(BaseModel):
    user = models.ForeignKey(User,null=True,blank=True ,on_delete=models.SET_NULL,related_name="carts")
    is_paid = models.BooleanField(default=False)
    instamojo_id = models.CharField(max_length=1000)
    def get_cart_total(self):
        return self.cart_items.aggregate(total=Sum('course__CoursePrice'))['total'] or 0
    


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
