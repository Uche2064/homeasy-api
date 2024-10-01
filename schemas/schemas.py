from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy import JSON
class Adresse(BaseModel):
    pays: Optional[str] = None
    ville: Optional[str] = None
    rue: Optional[str] = None
    region: Optional[str] = None
    quartier: Optional[str] = None
    

class BaseUtilisateur(BaseModel):
    uid: str
    nomComplet: str
    email: EmailStr = None
    adresse: Optional[Adresse] = None
    photoDeProfilUrl: Optional[str] = None
    numero: Optional[str] = None
    
    class Config:
        from_attributes: True
        
class AjouterUtilisateur(BaseUtilisateur):
    motDePasse: str
    
    class Config:
        from_attributes = True

class ReponseModelUtilisateur(BaseUtilisateur):
    dateCreation: Optional[datetime] = None
    dateModification: Optional[datetime] = None
    
class UpdateUtilisateur(BaseModel):
    nomComplet: Optional[str] = None
    adresse: Optional[Adresse] = None
    photoDeProfilUrl: Optional[str] = None
    numero: Optional[str] = None
    motDePasse: Optional[str] = None
    
    