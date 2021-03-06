from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .serializers import EmployeeSerializer, StoreSerializer, StoreDetailSerializer
from .utils import GeoLocation
from apps.employee.models import Employee
from apps.store.models import Store, Visit


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'


class EmployeeList(ListCreateAPIView):
    """
    View is used for create Employee
    """
    pagination_class = LargeResultsSetPagination
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailUpdateDestroy(RetrieveDestroyAPIView, UpdateAPIView, GenericAPIView):
    """
    View is used for get / update / delete Employee
    """
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class StoreList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    pagination_class = LargeResultsSetPagination

    def get(self, request, *args, **kwargs):
        """
        get Stores list
        """
        employee = request.user
        self.queryset = self.queryset.filter(employee__phone_number=employee.phone_number)
        return self.list(request, *args, **kwargs)


class StoreDetailUpdateDestroy(RetrieveDestroyAPIView, UpdateAPIView):
    """
    View is used for get / update / delete Store
    """
    permission_classes = (IsAuthenticated,)
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer

    def get(self, request, pk=None, *args, **kwargs):
        """
        get Store by pk
        """
        employee = request.user
        self.queryset = self.queryset.filter(employee__phone_number=employee.phone_number)

        store = get_object_or_404(self.queryset, pk=pk)
        data = GeoLocation(request)
        visit = Visit()
        visit.set_visit_store(store, data.get_ip, data.get_lat_long)

        serializer = StoreDetailSerializer(store)
        return Response(serializer.data)


def home(request):
    return JsonResponse(data={"message": "success"}, status=200)
