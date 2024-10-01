from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from psycopg2 import IntegrityError
from sqlalchemy import or_
from sqlalchemy.orm import Session
from config.http_exception import HttpException
from data.database import get_db
from data.models import Utilisateur
from schemas import schemas

router = APIRouter(
    prefix='/utilisateur',
    tags=["Utilisateur"],
)

@router.get("/", status_code=status.HTTP_200_OK,  response_model= List[schemas.ReponseModelUtilisateur])
def getUtilisateur(db: Session = Depends(get_db)):
    return db.query(Utilisateur).all()
    
    
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ReponseModelUtilisateur)
def getUtilisateur(id: str ,db: Session = Depends(get_db)):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.uid == id).first()
    if utilisateur is None:
        return HttpException(code=404, message="Utilisateur non trouvé")
    return utilisateur

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ReponseModelUtilisateur)
def save_user_record(utilisateur: schemas.AjouterUtilisateur, db: Session = Depends(get_db)):
    try:
        get_utitlisateur = db.query(Utilisateur).filter(or_(Utilisateur.email == utilisateur.email, Utilisateur.numero == utilisateur.numero)).first()
        if get_utitlisateur:
            raise HttpException(message="Utilisateur existe déjà", code=403)
        
        new_utilisateur = Utilisateur(**utilisateur.model_dump())
        db.add(new_utilisateur)
        db.commit()
        db.refresh(new_utilisateur)
        return new_utilisateur
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{uid}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ReponseModelUtilisateur)
def update_user_record(uid: str, updated_utilisateur: schemas.UpdateUtilisateur, db: Session = Depends(get_db)):
    try:
        get_utilisateur = db.query(Utilisateur).filter(Utilisateur.uid == uid).first()
        if get_utilisateur is None:
            raise HttpException(code=404, message="Utilisateur non trouvé")
        
        update_utilisateur = updated_utilisateur.model_dump(exclude_unset=True)
        
        for key, value in update_utilisateur.items():
            setattr(get_utilisateur, key, value)        
        get_utilisateur.dateModification = datetime.now()
        db.commit()
        db.refresh(get_utilisateur)
        return get_utilisateur
    except Exception as e :
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))