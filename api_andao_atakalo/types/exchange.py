from graphene_django import DjangoObjectType
from ..models import Exchange

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