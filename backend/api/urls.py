from django.urls import include, path
from api import views

# StoreCreateView

urlpatterns = [
    path('employees/', views.EmployeeList.as_view(), name='employees'),
    path('employee-detail/<int:pk>/', views.EmployeeDetailUpdateDestroy.as_view(), name='employee_get'),

    path('store-list/', views.StoreViewSet.as_view({'get': 'list'}), name='store_list'),
    path('store-detail/<int:pk>/', views.StoreDetailUpdateDestroy.as_view(), name='store_detail'),
    path('store-create/', views.StoreCreateView.as_view(), name='store_create'),

    path('', views.home, name="home"),
]