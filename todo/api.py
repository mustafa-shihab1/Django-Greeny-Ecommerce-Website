from .serializers import ToDoSerializer
from .models import ToDo
from rest_framework import viewsets


'''
    CRUD Operations:
    
        1. Functions {{ 1-function || 4-functions -> [list-create-update-delete] }}
        2. Classes:
            - Basic-Views {{ 1-class -> [list-create-update-delete] }}
            - Generic     {{ ListCreate class + UpdateDestroy class }}
            - Viewsets    {{ 1-class for all crud op.  && url-> router }}
        
'''
### Viewsets
class ToDoAPIViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer



### 1) Functions (1-function)
# def todo(request):
#     if request.method == 'GET':
#         pass
#     if request.method == 'POST':
#         pass
#     if request.method == 'PUT':
#         pass
#     if request.method == 'DELETE':
#         pass

### 2) Classes (Basic Views -> 1-class)
# class TodoAPI(ListAPI):
#     def get():
#         pass
#     def post():
#         pass
#     def put():
#         pass
#     def delete():
#         pass
    