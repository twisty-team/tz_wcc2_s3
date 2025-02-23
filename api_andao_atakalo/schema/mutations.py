import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

from ..types import ExchangeType, PictureType, OwnerType
from ..models import Exchange, Owner, Picture


class CreateExchangeMutation(graphene.Mutation):
    exchange = graphene.Field(ExchangeType)
    success = graphene.Boolean()
    
    class Arguments:
        user_name = graphene.String()
        contact = graphene.String()
        toy_to_change = graphene.String()
        desired_toy = graphene.String()


    def mutate(self, info, user_name, contact, toy_to_change, desired_toy):
        owner = Owner.objects.filter(name=user_name, contact=contact)
        
        if len(owner) == 0 :
            owner = Owner.objects.create(name=user_name, contact=contact)
        else:
            owner = owner[0]
        exchange = Exchange.objects.create(
            owner=owner,
            toy_to_change=toy_to_change,
            desired_toy=desired_toy,
        )
        files = info.context.FILES.getlist("0")
        for file in files:
            picture = Picture(exchange=exchange, image_url=file)
            picture.save()
        return CreateExchangeMutation(exchange=exchange, success=True)


class DeactivateExchangeMutation(graphene.Mutation):
    message = graphene.String()
    exchange = graphene.Field(ExchangeType)
    
    class Arguments:
        id = graphene.ID()

    def resolve_message(self, info, **kwargs):
        return "Exchange deactivated successfully"

    @classmethod
    def mutate(cls, root, info, id):
        exchange = Exchange.objects.get(id=id)
        exchange.active = False
        exchange.save()
        return DeactivateExchangeMutation(exchange=exchange)


class Mutation(graphene.ObjectType):
    create_exchange = CreateExchangeMutation.Field()
    deactivate_exchange = DeactivateExchangeMutation.Field()
