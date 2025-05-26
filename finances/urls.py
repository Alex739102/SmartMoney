
from django.urls import path
from .views import TransactionCreateView, CategoryCreateView, CategoryListView, CategoryDeleteView, TransactionListView, \
    TransactionDetailView, TransactionUpdateView, TransactionDeleteView

urlpatterns = [

    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('transaction/create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction_list/', TransactionListView.as_view(), name='transaction_list'),
    path('transaction_details/<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('transaction/update/<int:pk>/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transaction/delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction_delete'),

]