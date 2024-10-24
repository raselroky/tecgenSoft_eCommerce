from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView, ListAPIView,
    RetrieveDestroyAPIView,RetrieveAPIView
)
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.utils.decorators import method_decorator
from .models import (
    Notification
)
from .serializers import AdminNotificationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Case, When

from django.http import HttpResponse
from rest_framework.views import APIView

from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist





class AdminNotificationListAPIView(ListAPIView):
    permission_classes=(AllowAny,)
    queryset=Notification.objects.filter()
    serializer_class=AdminNotificationSerializer
    search_fields = ['title', 'verb', 'message']

    def get_queryset(self):
        
        qs=Notification.objects.all().order_by(
            Case(
                When(is_read=False, then=0),
                default=1
            ),
            '-created_at'
        )
        return qs


class AdminNotificationRetrieveDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Notification.objects.all()
    serializer_class=AdminNotificationSerializer
    lookup_field='id'

    def get_queryset(self):
        current_user=self.request.user
        qs=Notification.objects.all().order_by('-created_at')
        return qs
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # if instance.created_by != request.user:
        #     return Response({"message": "You do not have permission to update this notification."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # if instance.created_by != request.user:
        #     return Response({"message": "You do not have permission to delete this notification."}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({"message": "Notification deleted successfully."}, status=status.HTTP_200_OK)



class UsersNotificationListAPIView(ListAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Notification.objects.filter()
    serializer_class=AdminNotificationSerializer
    search_fields = ['$title', '$verb', '$message']

    def get_queryset(self):
        current_user=self.request.user
        qs=Notification.objects.filter(recipient=current_user).order_by(
            Case(
                When(is_read=False, then=0),
                default=1
            ),
            '-created_at'
        )
        return qs

class UsersNotificationRetrieveAPIView(RetrieveAPIView):
    permission_classes=(IsAuthenticated,)
    queryset=Notification.objects.filter()
    serializer_class=AdminNotificationSerializer
    lookup_field='id'

    def get_queryset(self):
        current_user=self.request.user
        qs=Notification.objects.filter(recipient=current_user).order_by(
            Case(
                When(is_read=False, then=0),
                default=1
            ),
            '-created_at'
        )
        return qs

# class ExportExcelAPIView(APIView):
#     permission_classes = [AllowAny]
#     def get(self, request, *args, **kwargs):
#         # Fetch data and generate Excel as before
#         model_type = request.query_params.get('model_type')
#         if model_type:
#             data = CommissionShare.objects.filter(model_type=model_type)
#         else:
#             return Response({"message":"please model_type not select!"},status=status.HTTP_400_BAD_REQUEST)
#         serializer = CommissionShareSerializerCustom(data, many=True)
#         df = pd.DataFrame(serializer.data)

#         response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#         response['Content-Disposition'] = 'attachment; filename=CommissionShare_data.xlsx'

#         with pd.ExcelWriter(response, engine='openpyxl') as writer:
#             df.to_excel(writer, sheet_name='Data', index=False)

#         return response




# class ImportExcelAPIView(APIView):
#     permission_classes = (AllowAny,)
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         # Get the uploaded file from the request
#         file = request.FILES.get('file')
#         if not file:
#             return JsonResponse({'error': 'No file provided'}, status=400)

#         # Read the Excel file into a DataFrame
#         try:
#             df = pd.read_excel(file)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#         # Process each row in the DataFrame
#         updated_records_count = 0
#         for index, row in df.iterrows():
#             model_type = row.get('model_type')
#             object_pk = row.get('object_pk')
#             share = row.get('share')

#             # Validate the necessary fields
#             if model_type is None or object_pk is None or share is None:
#                 continue  # Skip rows with missing values

#             # Update or create the record in the database
#             commission_share, created = CommissionShare.objects.update_or_create(
#                 model_type=model_type,
#                 object_pk=object_pk,
#                 defaults={'share': share}
#             )

#             updated_records_count += 1

#         return JsonResponse({'success': True, 'updated_records': updated_records_count}, status=200)