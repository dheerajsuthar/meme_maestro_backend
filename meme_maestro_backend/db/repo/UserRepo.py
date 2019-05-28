from . import BaseRepo


class UserRepo(BaseRepo):
    pass


if __name__ == '__main__':
    UserRepo().create({'name': 'Dheeraj Suthar',
                       'password': 'trial',
                       'email': 'd@e.com'})
