from graphene_django import DjangoObjectType
import graphene

from gardenapi.models import TankLevelReadingModel

class TankLevelReading(DjangoObjectType):
    class Meta:
        model = TankLevelReadingModel

class Query(graphene.ObjectType):
    TankLevelReading = graphene.List(TankLevelReading)

    def resolve_tank_level_readings(self, info):
        return TankLevelReading.objects.all()

schema = graphene.Schema(query=Query)