from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import dotenv_values, load_dotenv
load_dotenv(override=False)
environment = dotenv_values(".env")

db_host=environment['POSTGRES_HOST']
db_user=environment['POSTGRES_USER']
db_password=environment['POSTGRES_PASSWORD']
db_name=environment['DB_NAME']

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()