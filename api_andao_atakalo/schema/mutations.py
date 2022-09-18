import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

from ..types import ExchangeType, PictureType, OwnerType
from ..models import Exchange, Owner


class CreateExchangeMutation(graphene.Mutation):
    class Arguments:
        user_name = graphene.String()
        contact = graphene.String()
        toy_to_change = graphene.String()
        desired_toy = graphene.String()
        pictures = Upload(required=True)

    exchange = graphene.Field(ExchangeType)
    success = graphene.Boolean()

    def mutate(self, info, user_name, contact, toy_to_change, desired_toy, pictures):
        owner = Owner.objects.create(name=user_name, contact=contact)
        exchange = Exchange.objects.create(
            owner=owner,
            toy_to_change=toy_to_change,
            desired_toy=desired_toy,
            # pictures=pictures
        )
        # TODO : File upload
        # exchange.pictures = pictures.set()
        return CreateExchangeMutation(exchange=exchange)


class DeactivateExchangeMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    message = graphene.String()
    exchange = graphene.Field(ExchangeType)

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
