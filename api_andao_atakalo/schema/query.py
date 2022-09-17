from graphene_django import DjangoObjectType
import graphene

from ..utils import get_paginator

from ..types import ExchangeType
from ..models import Exchange

# Now we create a corresponding PaginatedType for that object type:
class ExchangePaginatedType(graphene.ObjectType):
    count = graphene.Int()
    currentPage = graphene.Int()
    totalPages = graphene.Int()
    next = graphene.String()
    prev = graphene.String()
    results = graphene.List(ExchangeType)



class Query(graphene.ObjectType):
    exchanges = graphene.Field(ExchangePaginatedType, page=graphene.Int())

    def resolve_exchanges(root, info, page=1,**kwargs):
        # Querying a list
        page_size = 10
        base_url = info.context.build_absolute_uri()
        qs = Exchange.objects.filter(active=True).order_by("-id")
        return get_paginator(qs, page_size, page, base_url, ExchangePaginatedType)
