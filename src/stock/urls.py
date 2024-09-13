from django.urls import path,include
from .views import StockListCreateAPIView,StockRetrieveUpdateDestroyAPIView,StockHistoryListCreateAPIView,StockHistoryRetrieveUpdateDestroyAPIView

urlpatterns=[
    path('stockcreate/',StockListCreateAPIView.as_view(),name='stock-create-api'),
    path('stock-retrieve-update-destroy/<int:id>',StockListCreateAPIView.as_view(),name='stock-retrieve-update-destroy-api'),

    path('stockhistorycreate/',StockHistoryListCreateAPIView.as_view(),name='stock-history-create-api'),
    path('stockhistory-retrieve-update-destroy/<int:id>',StockHistoryRetrieveUpdateDestroyAPIView.as_view(),name='stock-history-retrieve-update-destroy-api'),
]