# from django.db import models
# from django.contrib.auth.models import User

# import uuid
# class BaseModel(models.Model):
#     uid = models.UUIDField(default=uuid.uuid4 , editable=False, primary_key=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         abstract = True



# class Cart(BaseModel):
#     user = models.ForeignKey(User,null=True,blank=True ,on_delete=models.SET_NULL,related_name="cart")
#     is_paid = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Cart for {self.user.username}"

#     def total_price(self):
#         total = 0
#         for item in self.cart_items.all():
#             total += item.total_price()
#         return total
    

# class CartItem(BaseModel):
#     cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} x {self.course.CourseName}"

#     def total_price(self):
#         return self.quantity * self.course.CoursePrice