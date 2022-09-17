from graphene_django import DjangoObjectType
import graphene

from ..types import ExchangeType
from ..models import Exchange

class Query(graphene.ObjectType):
    exchanges = graphene.List(ExchangeType)

    def resolve_exchanges(root, info, **kwargs):
        # Querying a list
        return Exchange.objects.all()
