from django.shortcuts import render
from .serializers import TasksSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import TasksStore
from .configuration import constants

# API: view_tasks
# Description: This API will return all the tasks added by user
@api_view(['GET'])
def view_tasks(request):
    try:
        tasks = TasksStore.objects.all().order_by('-id')
        serializer = TasksSerializer(tasks, many=True)
        result = {
            constants.STATUS_CODE: constants.HTTP_200_CODE,
            constants.MESSAGE: constants.DATA_RETRIVED_SUCCESS,
            constants.DATA: serializer.data
        }
        return JsonResponse(result, safe=True)
    except Exception as error:
        print("error", error)
        result = {
                constants.STATUS_CODE: constants.HTTP_500_CODE,
                constants.MESSAGE: constants.SOMETHING_WENT_WRONG,
            }
        return JsonResponse(result, safe=True)

# API: create_task
# Description: This API will is used to create a new task
@api_view(['POST'])
def create_task(request):
    try:
        serializer = TasksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            result = {
                constants.STATUS_CODE: constants.HTTP_200_CODE,
                constants.MESSAGE: constants.CREATE_SUCCESS_MESSAGE,
            }
        return JsonResponse(result, safe=True)
    except Exception as error:
        print("error", error)
        result = {
                constants.STATUS_CODE: constants.HTTP_500_CODE,
                constants.MESSAGE: constants.SOMETHING_WENT_WRONG,
            }
        return JsonResponse(result, safe=True)

# API: update_tasks
# Description: This API is used to update an existing task 
@api_view(['POST'])
def update_task(request, id):
    try:
        task = TasksStore.objects.get(id=id)
        serializer = TasksSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            result = {
                constants.STATUS_CODE: constants.HTTP_200_CODE,
                constants.MESSAGE: constants.UPDATE_SUCCESS_MESSAGE,
            }
        return JsonResponse(result, safe=True)
    except Exception as error:
        print("error", error)
        result = {
                constants.STATUS_CODE: constants.HTTP_500_CODE,
                constants.MESSAGE: constants.SOMETHING_WENT_WRONG,
            }
        return JsonResponse(result, safe=True)


# API: delete_tasks
# Description: This API is used to  delete a particular task
@api_view(['DELETE'])
def delete_task(id):
    try:
        task = TasksStore.objects.get(id=id)
        task.delete()
        result = {
            constants.STATUS_CODE: constants.HTTP_200_CODE,
            constants.MESSAGE: constants.DELETED_SUCCESS_MESSAGE
        }
        return JsonResponse(result, safe=True)
    except Exception as error:
        print("error", error)
        result = {
                constants.STATUS_CODE: constants.HTTP_500_CODE,
                constants.MESSAGE: constants.SOMETHING_WENT_WRONG,
        }
        return JsonResponse(result, safe=True)