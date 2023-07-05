from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Task
from .serializers import TaskGetSerializer, TaskPostSerializer


class TaskView(ListAPIView, APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    queryset = Task.objects.all()
    serializer_class = TaskGetSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        param = self.request.query_params.get('q')
        if param == 'all':
            pass

        elif param == 'completed':
            queryset = queryset.filter(completed=True)

        elif param == 'not_completed':
            queryset = queryset.filter(completed=False)

        return queryset

    def post(self, request):
        serializer = TaskPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    @staticmethod
    def get_data(pk: int):
        try:
            return Task.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404("Data not found!!!")

    def get(self, request, pk):
        serializer = TaskGetSerializer(self.get_data(pk=pk))
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = TaskPostSerializer(self.get_data(pk=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "request": "your data is updated",
                "update_data": serializer.data
            },
                status=status.HTTP_200_OK)

        return Response({"request": "your data is not updated",
                         "error": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_data(pk=pk)
        try:
            task.delete()
            return Response(data={'request': 'Data successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            print(ex)
            return Response(data={'request': "qwe"}, status=status.HTTP_400_BAD_REQUEST)
