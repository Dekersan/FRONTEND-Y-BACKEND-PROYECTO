from pydantic import BaseModel, constr, PositiveInt, ValidationError

class guia(BaseModel):
    Num_guia: int
    Nom_remitente: str
    Id_remitente: int
    Origen : str
    Nom_destinatario : str
    Id_destinatario: int
    Destino : str
    Tipo_mercancia:str
    kilos: int
    flete: int
    total : int



    