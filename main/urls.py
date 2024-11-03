from django.urls import path

from main.views import CategoryListView , CategoryDetailView , test

urlpatterns = [
    path('', CategoryListView.as_view() , name='category_list'),
    path('category/<int:category_id>/', CategoryDetailView.as_view() , name='category_detail'), 
    path('test' ,test ,  name = 'test')

]

