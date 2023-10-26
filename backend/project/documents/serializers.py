from rest_framework import serializers
from .models import Documents , Annotation


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ('id','label','start','end','text')

class DocumentsSerializer(serializers.ModelSerializer):
    annotation = AnnotationSerializer(many=True)

    class Meta:
        model = Documents
        fields = '__all__'

    def update(self, instance, validated_data):
        annotation_data = validated_data.pop('annotation')
        instance.annotation.clear()  # Remove existing annotations

        for annotation_item in annotation_data:
            label = annotation_item['label']
            start = annotation_item['start']
            end = annotation_item['end']
            text = annotation_item['text']
            annotation, created = Annotation.objects.get_or_create(label=label, start=start, end=end, text=text)
            instance.annotation.add(annotation)

        instance.document = validated_data.get('document', instance.document)
        instance.save()
        return instance
