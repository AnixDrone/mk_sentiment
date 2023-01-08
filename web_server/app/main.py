from typing import Optional
from sqlalchemy.orm import Session
from typing import List
import time

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud
from . import models
from . import schemas
from .database import SessionLocal, engine
from sqlalchemy.exc import OperationalError

for i in range(10):
    try:
        models.Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        time.sleep(i+1)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/sentence", response_model=schemas.Sentence)
def get_unlabeled_sentece(
    db: Session = Depends(get_db)
):
    sentence = crud.get_unlabeled_sentece(db)
    return sentence


@app.get("/random_sentence", response_model=schemas.Sentence)
def get_random_sentence(
    db: Session = Depends(get_db)
):
    sentence = crud.get_random_sentence(db)
    return sentence


@app.get("/sentence/{sentence_id}", response_model=schemas.Sentence)
def get_sentence(sentence_id: int, db: Session = Depends(get_db)):
    return crud.get_sentence(db, sentence_id)


@app.post("/sentence", response_model=schemas.Sentence)
def create_sentence(sentence: schemas.SentenceBase, db: Session = Depends(get_db)):
    db_sentence = crud.get_sentence_by_sentence(db, sentence.sentence)
    if db_sentence is not None:
        raise HTTPException(status_code=400, detail="Sentence already exist")
    return crud.create_sentece(db=db, sentence_base=sentence)


@app.get("/sentence/{sentence_id}/{label}", response_model=schemas.Sentence)
def label_sentence(sentence_id: int, label: int, db: Session = Depends(get_db)):
    db_sentence = crud.label_sentence(
        db=db, sentence_id=sentence_id, label=label)
    return db_sentence
