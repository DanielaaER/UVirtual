from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB
from config.db import meta_data


estudiante = Table("clases", metadata,
                   Column("nrc", Integer(6),
                          primary_key=True, nullable=False),
                   Column("nombre", VARCHAR(50), nullable=False),
                   Column("DocenteId", varchar(10),
                          ForeingKey(), nullable=False),
                   Column("AulaID", integer(2),
                          ForeingKey(), nullable=False),
                   )

meta_data.bind = engine
meta_data.create_all()
