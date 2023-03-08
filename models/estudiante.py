from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB
from config.db import meta_data


estudiante = Table("estudiante", metadata,
                   Column("matricula", VARCHAR(10), nullable=false),
                   Column("nombre", VARCHAR(200), nullable=False),
                   Column("telefono", Integer(10), nullable=false),
                   Column("correo", char(18), nullable=false),
                   Column("facultad", VARCHAR(100), nullable=false),
                   Column("campus", VARCHAR(50), nullable=false),
                   Column("semestre", Interger, nulleable=false),
                   Column("periodo", VARCHAR(50), nulleable=false),
                   Column("fotografia", BLOB, nulleable=false)


                   ) 

meta_data.bind = engine
meta_data.create_all()
