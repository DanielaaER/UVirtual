from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')