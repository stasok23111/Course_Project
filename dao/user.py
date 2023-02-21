from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, data):
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update(self, data):
        user = self.get_by_email(data.get('email'))
        user.name = data.get('name')
        user.surname = data.get('surname')
        user.favorite_genre = data.get('favorite_genre')

        self.session.add(user)
        self.session.commit()

    def update_password(self, data):
        user = self.get_by_email(data.get('email'))
        user.password = data.get('other_password')
        self.session.add(user)
        self.session.commit()