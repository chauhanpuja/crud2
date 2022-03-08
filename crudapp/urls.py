from django.urls import path
from . import views

urlpatterns = [
   path('',views.addandshow),
   path('delete/<int:id>',views.delete_data),
   path('update=<int:id>',views.update_data),
   path('signup',views.signup),
   path('userlogin',views.userlogin),
   path('userlogout',views.userlogout),

]