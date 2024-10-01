from sqlalchemy import Column, ForeignKey, String, Integer, JSON, ARRAY, Float ,DateTime, Boolean
from datetime import datetime
from .database import Base
from sqlalchemy.orm import relationship



class Utilisateur(Base):
    __tablename__ = "utilisateur"
    uid = Column(String, nullable=False, primary_key=True)
    nomComplet = Column(String, nullable=False)
    numero = Column(String, nullable=True, unique=True)
    email = Column(String, nullable=False, unique=True)
    photoDeProfilUrl = Column(String, nullable=True)
    motDePasse = Column(String, nullable=False)
    adresse =  Column(JSON, nullable=True)   
    estActive = Column(Boolean, nullable=False, default=True)
    dateCreation = Column(DateTime, nullable=True, default=datetime.now())
    dateModification = Column(DateTime, nullable=True, default=datetime.now())
    
    # relationships
    # maisons = relationship("Maison", back_populates="utilisateur")
    # favoris = relationship("Favoris", back_populates="utilisateur")
    # reservations = relationship("Reservation", back_populates="utilisateur")
    # offres = relationship("Offre", back_populates="utilisateur")
    # annonce = relationship("Annonce", back_populates="utilisateur")
    # discussions = relationship("Discussion", back_populates="utilisateur")
    
    
class Maison(Base):
    __tablename__ = "maison"
    mid = Column(String, nullable=False, primary_key=True)
    prix = Column(Float, nullable=True)
    photosUrl = Column(ARRAY(String), nullable=True)
    adresse =  Column(JSON, nullable=True)
    frequenceDePaiement = Column(String, nullable=True)
    caracteristiqueMaison = Column(JSON, nullable=True)
    uid = Column(String, ForeignKey('utilisateur.uid'), nullable=False)
    dateCreation = Column(DateTime, nullable=True, default=datetime.now())
    dateModification = Column(DateTime, nullable=True, default=datetime.now())
    
    # relationships
    # utilisateur = relationship("Utilisateur", back_populates="maisons")
    # favoris = relationship("Favoris", back_populates="maison")
    # reservations = relationship("Reservation", back_populates="maison")
    # offres = relationship("Offre", back_populates="maison")
    # annonce = relationship("Annonce", back_populates="maison")
    # discussions = relationship("Discussion", back_populates="maison")

class Favoris(Base):
    __tablename__ = "favoris"
    fid = Column(String, nullable=False, primary_key=True)
    uid = Column(String, ForeignKey('utilisateur.uid'), nullable=False)
    mid = Column(String, ForeignKey('maison.mid'), nullable=False)
    dateCreation = Column(DateTime, nullable=True, default=datetime.now())
    dateModification = Column(DateTime, nullable=True, default=datetime.now())
    
    # relationship
    # utilisateur = relationship("Utilisateur", back_populates="favoris")
    # maison = relationship("Maison", back_populates="favoris")
    
    
    
class Reservation(Base):
    __tablename__ = "reservation"
    rid = Column(String, nullable=False, primary_key=True)
    uid = Column(String, ForeignKey('utilisateur.uid'), nullable=False)
    mid = Column(String, ForeignKey('maison.mid'), nullable=False)
    dateCreation = Column(DateTime, nullable=True, default=datetime.now())
    dateModification = Column(DateTime, nullable=True, default=datetime.now())
    
    # relationship
    # utilisateur = relationship("Utilisateur", back_populates="reservations")
    # maison = relationship("Maison", back_populates="reservations")
    
class Annonce(Base):
    __tablename__ = "annonce"
    aid = Column(String, nullable=False, primary_key=True)
    uid = Column(String, ForeignKey('utilisateur.uid'), nullable=False)
    mid = Column(String, ForeignKey('maison.mid'), nullable=False)
    description = Column(String, nullable=False)
    datePublication = Column(DateTime, nullable=True, default=datetime.now())
    dateModification = Column(DateTime, nullable=True, default=datetime.now())
    
    # relationship
    # utilisateur = relationship("Utilisateur", back_populates="annonces")
    # maison = relationship("Maison", back_populates="annonces")
    
class Offre(Base):
    __tablename__ = "offre"
    oid = Column(String, nullable=False, primary_key=True)
    uid = Column(String, ForeignKey('utilisateur.uid'), nullable=False)
    mid = Column(String, ForeignKey('maison.mid'), nullable=False)
    statut = Column(String, nullable=True)
    dateCreation = Column(DateTime, nullable=True, default=datetime.now())
    dateModification = Column(DateTime, nullable=True, default=datetime.now())    
    
    # relationship
    # utilisateur = relationship("Utilisateur", back_populates="offres")
    # maison = relationship("Maison", back_populates="offres")
    
class Discussion(Base):
    __tablename__ = "discussion"
    did = Column(String, nullable=False, primary_key=True)
    u1id = Column(String, ForeignKey('utilisateur.uid'), nullable=False)
    u2id = Column(String, ForeignKey('utilisateur.uid'), nullable=False)
    messages = Column(ARRAY(String))
    mid = Column(String, ForeignKey('maison.mid'), nullable=False)
    dernierMmessage = Column(String, nullable=False)
    
    dateCreation = Column(DateTime, nullable=True, default=datetime.now())
    dateModification = Column(DateTime, nullable=True, default=datetime.now())
    
    # relationship
    # utilisateur = relationship("Utilisateur", back_populates="discussions")
    # maison = relationship("Maison", back_populates="discussions")
    