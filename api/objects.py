from api.models import Place

# criar objetos do tipo Place(hardcoded)
def createPlaces():
    # save() salva o objeto no banco
    place1 = Place(id = 1, name = "Parque da Cidade", latitude = -23.221112, longitude = -45.899678)
    place1.save()

    place2 = Place(id = 2, name = "Praça Ulisses Guimarães", latitude = -23.180038, longitude = -45.884357)
    place2.save()

    place3 = Place(id = 3, name = "Parque Tecnológico", latitude = -23.15688, longitude = -45.79273)
    place3.save()

    place6 = Place(id = 6, name = "Rodoviária Velha", latitude = -23.10688, longitude = -45.79073)
    place6.save()

    places = [place1, place2, place3, place6]
    return places

    