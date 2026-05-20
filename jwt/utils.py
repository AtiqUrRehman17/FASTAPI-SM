from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'],deprecated='auto') # for hashing the password

fake_user_db = {
    'johndoe':{
        'username':'johndoe',
        'hashed_password':pwd_context.hash('secret123')
    }
}

# utility functions
def get_user(username:str):
    user = fake_user_db.get(username)
    return user


def varify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)