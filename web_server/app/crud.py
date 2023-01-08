from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func, select
import random

from . import models
from . import schemas


def get_sentence(db: Session, sentence_id: int):
    return db.query(models.Sentences).filter(models.Sentences.id == sentence_id).first()


def get_random_sentence(db: Session):
    return db.query(models.Sentences).order_by(func.random()).filter(models.Sentences.labeled==3).first()


def get_unlabeled_sentece(db: Session):
    return db.query(models.Sentences).filter(models.Sentences.labeled == 3).first()


def get_sentence_by_sentence(db: Session, sentence: str):
    return db.query(models.Sentences).filter(models.Sentences.sentence == sentence).first()


def create_sentece(db: Session, sentence_base: schemas.SentenceBase):
    db_sentence = models.Sentences(sentence=sentence_base.sentence)
    db.add(db_sentence)
    db.commit()
    db.refresh(db_sentence)
    return schemas.Sentence(id=db_sentence.id, sentence=db_sentence.sentence, labeled=db_sentence.labeled)


def label_sentence(db: Session, sentence_id: int, label: int):
    db_sentence = db.query(models.Sentences).filter(
        models.Sentences.id == sentence_id).first()
    db_sentence.labeled = label
    db.commit()
    db.refresh(db_sentence)
    return db_sentence
