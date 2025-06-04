class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.bd"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class TestingConfig(Config):
    TESTING = True
    TESTING = SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    