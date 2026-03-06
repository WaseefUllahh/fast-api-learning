from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "string"

hashedPassword = pwd_cxt.hash(password[:72])
