from models.user import User
from sqlalchemy.orm import Session
from dto import user

def create_user(data:user.User,db:Session):
    user = User(
        name=data.name,
        email=data.email,
        phone=data.phone
    )

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)

    return user

def get_user(id:int,db:Session):
    return db.query(User).filter(User.id==id).first()


def get_all_users(db:Session):
    return db.query(User).all()

def update(data:user.User,db:Session,id:int):
    user = db.query(User).filter(User.id==id).first()
    user.name = data.name
    user.email = data.email
    user.phone = data.phone
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def remove(db:Session,id:int):
    user = db.query(User).filter(User.id == id).delete()
    db.commit()
    return user