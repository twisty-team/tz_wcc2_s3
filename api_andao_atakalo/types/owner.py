from graphene_django import DjangoObjectType
from ..models import Owner

class OwnerType(DjangoObjectType):
    class Meta: 
        model = Owner
        fields = ('id','name', 'contact')
