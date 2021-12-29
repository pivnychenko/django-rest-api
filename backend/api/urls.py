from django.urls import include, path
from api import views

# StoreCreateView

urlpatterns = [
    path('employees/', views.EmployeeList.as_view(), name='employees'),
    path('employee-detail/<int:pk>/', views.EmployeeDetailUpdateDestroy.as_view(), name='employee_get'),

    path('store-detail/<int:pk>/', views.StoreListDetailUpdateDestroy.as_view(), name='store_detail'),
    path('store-list/', views.StoreListDetailUpdateDestroy.as_view(), name='store_list'),

    path('', views.home, name="home"),
]