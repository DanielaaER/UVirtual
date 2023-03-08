from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR
from config.db import meta_data


login = Table("login", meta_data,
              Column("matricula", char(10), primary_key=true),
              Column("contraseña", VARCHAR(40), nullable=False)
              )

meta_data.bind = engine
meta_data.create_all()
