from .views import  CreateDocumentApiView , GetDocuments , GetAnnotationByHotelId, CreateAnnotationApiView , UpdateAnnotationApiView,UpdateDocumentApiView
from django.urls import path

urlpatterns = [

 
    path('list-documents/', GetDocuments.as_view(),name="list-annotations"),
    path('annotation/create/', CreateAnnotationApiView.as_view(),name="create-annotations"),
    path('annotation/<int:pk>/update/', UpdateAnnotationApiView.as_view(),name="update-annotations"),

    path('list-annotations/', GetAnnotationByHotelId.as_view(),name="list-documents"),
    path('create/', CreateDocumentApiView.as_view(),name="create-documents"),
    path('<int:pk>/update/', UpdateDocumentApiView.as_view(),name="update-documents"),
]