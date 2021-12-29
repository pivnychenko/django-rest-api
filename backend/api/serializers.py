from apps.employee.models import Employee
from apps.store.models import Store
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'name', 'phone_number', 'password']


class StoreSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.filter(admin=False), required=True)

    class Meta:
        model = Store
        fields = ['title', 'user', 'get_absolute_url']


class StoreDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ['id', 'title']


