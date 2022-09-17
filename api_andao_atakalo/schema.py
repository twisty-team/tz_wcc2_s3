import graphene
from graphene_django import DjangoObjectType
from .models import Owner, Exchange, Picture

class OwnerType(DjangoObjectType):
    class Meta: 
        model = Owner
        fields = ('id','name', 'contact')

  
class ExchangeType(DjangoObjectType):
    class Meta: 
        model = Exchange
        fields = (
            'id',
            'toy_to_change',
            'desired_toy',
            'owner',
            'pictures',
            'active'
        )  

class PictureType(DjangoObjectType):
    class Meta:
        model = Picture
        fields = (
            'id',
            'image_url',
            'exchange'
        )

class Query(graphene.ObjectType):
    exchanges = graphene.List(ExchangeType)

    def resolve_owners(root, info, **kwargs):
        # Querying a list
        return Owner.objects.all()

    def resolve_exchanges(root, info, **kwargs):
        # Querying a list
        return Exchange.objects.all()

    def resolve_pictures(root, info, **kwargs):
        # Querying a list
        return Picture.objects.all()

schema = graphene.Schema(query=Query)