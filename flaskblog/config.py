import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgres://vxhmugsbghxmaz:21966913fa0bf6160de91fe52fdb880c68b26056c1ad4a5fe817e59eb9db3dc4@ec2-3-217-14-181.compute-1.amazonaws.com:5432/ddgu6tpog670s3'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')