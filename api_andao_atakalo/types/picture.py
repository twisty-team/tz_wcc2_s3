from graphene_django import DjangoObjectType
from ..models import Picture

class PictureType(DjangoObjectType):
    class Meta:
        model = Picture
        fields = (
            'id',
            'image_url',
            'exchange'
        )