from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB
from config.db import meta_data


estudiante = Table("aulas", metadata,
                   Column("id_aula", Integer(2),
                          primary_key=True, nullable=False),
                   Column("edificio", integer(2), nullable=False),
                   Column("FacultadId", varchar(10),
                          ForeingKey(), nullable=False),
                   )

meta_data.bind = engine
meta_data.create_all()
