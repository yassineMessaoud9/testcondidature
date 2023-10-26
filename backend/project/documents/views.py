from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from .models import Documents , Annotation
from .serializers import DocumentsSerializer , AnnotationSerializer
from rest_framework.generics import ListAPIView

class GetDocuments(ListAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('annotation')  # Assumes you have a related name 'annotations'
        return queryset
class GetAnnotationByHotelId(ListAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer 

class CreateDocumentApiView(CreateAPIView):
    """ 
    this view can create  Documents 
    Requires the user to be a hotel admin.
    """

    serializer_class = DocumentsSerializer
    queryset = Documents.objects.all()

class UpdateDocumentApiView(UpdateAPIView):
    """ 
    this view can update  Documents 
    Requires the user to be a hotel admin.
    """
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer



class CreateAnnotationApiView(CreateAPIView):
    """ 
    this view can create  Annotation 
    Requires the user to be a hotel admin.
    """

    serializer_class = AnnotationSerializer
    queryset = Annotation.objects.all()

class UpdateAnnotationApiView(UpdateAPIView):
    """ 
    this view can update  Documents 
    Requires the user to be a hotel admin.
    """
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer

# Create your views here.


