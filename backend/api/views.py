from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .serializers import EmployeeSerializer, StoreSerializer, StoreDetailSerializer
from .utils import GeoLocation
from apps.employee.models import Employee
from apps.store.models import Store, Visit

class EmployeeList(ListCreateAPIView):
    """
    View is used for create Employee
    """
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailUpdateDestroy(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    """
    View is used for get / update / delete Employee
    """
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StoreListDetailUpdateDestroy(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    ListCreateAPIView):
    """
    View is used for get / update / delete Store
    """
    permission_classes = (IsAuthenticated,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get(self, request, pk=None, *args, **kwargs):
        """
        get Stores list or get Store by pk
        """
        employee = request.user
        queryset = Store.objects.filter(employee__phone_number=employee.phone_number)
        if not pk:
            serializer = StoreSerializer(queryset, many=True)
            return Response(serializer.data)

        store = get_object_or_404(queryset, pk=pk)

        data = GeoLocation(request)
        visit = Visit()
        visit.set_visit_store(store, data.get_ip, data.get_lat_long)

        serializer = StoreDetailSerializer(store)
        return Response(serializer.data)


def home(request):
    return JsonResponse(data={"message": "success"}, status=200)
