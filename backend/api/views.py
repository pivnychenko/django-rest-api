from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListCreateAPIView, GenericAPIView
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .serializers import EmployeeSerializer, StoreSerializer, StoreDetailSerializer
from .utils import GeoLocation
from apps.employee.models import Employee
from apps.store.models import Store, Visit
from api.authentication import ExampleAuthentication

class EmployeeList(ListCreateAPIView):
    """
    View is used for create Employee
    """
    permission_classes = (ExampleAuthentication,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailUpdateDestroy(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    """
    View is used for get / update / delete Employee
    """
    permission_classes = (ExampleAuthentication,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StoreViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing store.
    """
    permission_classes = (ExampleAuthentication,)

    def list(self, request):
        employee = request.user
        queryset = Store.objects.filter(user__phone_number=employee.phone_number)
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)


class StoreCreateView(CreateAPIView):
    """
    View is used for create Store
    """
    permission_classes = (ExampleAuthentication,)

    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StoreDetailUpdateDestroy(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    """
    View is used for get / update / delete Store
    """
    permission_classes = (ExampleAuthentication,)
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer

    def get(self, request, pk=None):
        employee = request.user
        queryset = Store.objects.filter(user__phone_number=employee.phone_number)
        store = get_object_or_404(queryset, pk=pk)

        data = GeoLocation(request)
        visit = Visit()
        visit.set_visit_store(store, data.get_ip, data.get_lat_long)

        serializer = StoreDetailSerializer(store)
        return Response(serializer.data)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def home(request):
    return JsonResponse(data={"message": "success"}, status=200)
