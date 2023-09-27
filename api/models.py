from ninja import Schema


class TagSchema(Schema):
    tagId: int
    nombre: str
    descripcion: str


class OSCSchema(Schema):
    oscId: int
    nombre: str
    alias: str
    tags: list[TagSchema]
    direccion: str
    coordenadas_latitud: float
    coordenadas_longitud: float
    email: str
    telefono: str
    areaContacto: str
    horaAtencion: str
    paginaWeb: str
