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
    edad = graphene.Int()
    nacionalidad = graphene.String()
    estatura = graphene.Int()
    peso = graphene.Int()
    club = graphene.String()
    posicion = graphene.String()
    goles = graphene.Int()
    asistencias = graphene.Int()
    imagen = graphene.String()

    #2
    class Arguments:
        nombre = graphene.String()
        edad = graphene.Int()
        nacionalidad = graphene.String()
        estatura = graphene.Int()
        peso = graphene.Int()
        club = graphene.String()
        posicion = graphene.String()
        goles = graphene.Int()
        asistencias = graphene.Int()
        imagen = graphene.String()

    #3
    def mutate(self, info, nombre, edad, nacionalidad, estatura, peso, club, posicion, goles, asistencias, imagen):
        link = Link(nombre=nombre, edad=edad, nacionalidad=nacionalidad, estatura=estatura, peso=peso, club=club, posicion=posicion,
            goles=goles, asistencias=asistencias, imagen=imagen)
        link.save()

        return CreateLink(
            id=link.id,
            nombre=link.nombre,
            edad=link.edad,
            nacionalidad=link.nacionalidad,
            estatura=link.estatura,
            peso=link.peso,
            club=link.club,
            posicion=link.posicion,
            goles=link.goles,
            asistencias=link.asistencias,
            imagen=link.imagen,
        )


#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()

