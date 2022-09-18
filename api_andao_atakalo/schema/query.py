from graphene_django import DjangoObjectType
import graphene

from ..utils import get_paginator

from ..types import ExchangeType
from ..models import Exchange


class ExchangePaginatedType(graphene.ObjectType):
    count = graphene.Int()
    page_size = graphene.Int()
    current_page = graphene.Int()
    total_pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    exchanges = graphene.List(ExchangeType)



class Query(graphene.ObjectType):
    paginated_exchanges = graphene.Field(ExchangePaginatedType, page_size=graphene.Int(), page=graphene.Int())

    def resolve_paginated_exchanges(root, info, page_size=10, page=1,**kwargs):
        qs = Exchange.objects.filter(active=True).order_by("-id")
        return get_paginator(qs, page_size, page, ExchangePaginatedType)
