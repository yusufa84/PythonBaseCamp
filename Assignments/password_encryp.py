from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

pw_hash = bcrypt.generate_password_hash('yusuf1')
# $2b$12$fkIQWRXUwJ5v976MsvCKruSlJ2XKZLsaUjvnor62bhY7igOGdFcH2
print(pw_hash)