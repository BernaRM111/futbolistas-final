import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()
    

#1
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    nacionalidad = graphene.String()
    posicion = graphene.String()
    club = graphene.String()
    goles = graphene.Int()
    edad = graphene.Int()
    estatura = graphene.Int()
    peso = graphene.Int()
    asistencias = graphene.Int()
    imagen = graphene.String()

    #2
    class Arguments:
        nombre = graphene.String()
        nacionalidad = graphene.String()
        posicion = graphene.String()
        club = graphene.String()
        goles = graphene.Int()
        edad = graphene.Int()
        estatura = graphene.Int()
        peso = graphene.Int()
        asistencias = graphene.Int()
        imagen = graphene.String()

    #3
    def mutate(self, info, nombre, nacionalidad, posicion, club, goles, edad, estatura, peso, asistencias, imagen):
        link = Link(
            nombre=nombre,
            nacionalidad=nacionalidad,
            posicion=posicion,
            club=club,
            goles=goles,
            edad=edad,
            estatura=estatura,
            peso=peso,
            asistencias=asistencias,
            imagen=imagen
        )
        link.save()

        return CreateLink(
            id=link.id,
            nombre=link.nombre,
            nacionalidad=link.nacionalidad,
            posicion=link.posicion,
            club=link.club,
            goles=link.goles,
            edad=link.edad,
            estatura=link.estatura,
            peso=link.peso,
            asistencias=link.asistencias,
            imagen=link.imagen,
        )


#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()

