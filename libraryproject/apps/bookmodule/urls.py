from django.urls import path
from . import views
urlpatterns = [
     
    
    path('<int:bookId>', views.viewbook) #
]
