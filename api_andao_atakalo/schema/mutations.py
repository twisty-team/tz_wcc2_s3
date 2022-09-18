from graphene_django import DjangoObjectType
import graphene

from ..types import ExchangeType, PictureType, OwnerType
from ..models import Exchange

# class CreateExchangeMutation(graphene.Mutation):
#     pass

class DeactivateExchangeMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    message = graphene.String()
    exchange = graphene.Field(ExchangeType)

    def resolve_message(self, info, **kwargs):
        return "Exchange deactivated successfully"

    @classmethod
    def mutate(cls, root, info, id):
        exchange = Exchange.objects.get(pk=id)
        exchange.active = False 
        exchange.save()
        return DeactivateExchangeMutation(exchange=exchange)

class Mutation(graphene.ObjectType):
    create_exchange = None
    deactivate_exchange = DeactivateExchangeMutation.Field()