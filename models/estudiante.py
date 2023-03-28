from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB
from config.db import meta_data


estudiante = Table("estudiante", metadata,
                   Column("matricula", VARCHAR(10),
                          primary_key=True, nullable=False),
                   Column("nombre", VARCHAR(200), nullable=False),
                   Column("telefono", Integer(10), nullable=False),
                   Column("correo", char(18), nullable=False),
                   Column("campus", VARCHAR(50), nullable=False),
                   Column("semestre", Interger, nulleable=False),
                   Column("periodo", VARCHAR(50), nulleable=False),
                   Column("fotografia", BLOB, nulleable=False),
                   Column("LoginMatricula", varchar(10), ForeingKey(), nullable=False),
                   Column("FacultadId", varchar(10), ForeingKey(), nullable=False),
                   Column("VisitaBibioteca", varchar(10), ForeingKey(), nullable=False)

                   )

meta_data.bind = engine
meta_data.create_all()
