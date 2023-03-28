from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB
from config.db import meta_data


estudiante = Table("docentes", metadata,
                   Column("id_docente", VARCHAR(10),
                          primary_key=True, nullable=False),
                   Column("nombre", VARCHAR(200), nullable=False),
                   Column("telefono", Integer(10), nullable=False),
                   Column("correo", char(18), nullable=False),
                   Column("campus", VARCHAR(50), nullable=False),
                   Column("fotografia", BLOB, nulleable=False),
                   Column("LoginTrabajador", varchar(10), ForeingKey(), nullable=False),
                   Column("FacultadId", varchar(10), ForeingKey(), nullable=False),
                  
                   )

meta_data.bind = engine
meta_data.create_all()
