import os

class Config:
    SECRET_KEY='abc123'
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:Limit168@localhost/twittor'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWEET_PER_PAGE = 2
