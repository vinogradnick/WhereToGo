from rest_framework import routers, serializers, viewsets

from web.models import University


class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = ('id', 'name', 'image', 'nums')


# ViewSets define the view behavior.
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
