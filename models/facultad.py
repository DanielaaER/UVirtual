from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB, DateTime, Time
from config.db import meta_data


estudiante = Table("facultades", metadata,
                   Column("id_facultad", Integer(4),
                          primary_key=True, nullable=False),
                   Column("nombre", VARCHAR(50), nullable=False),
                   Column("hora_inicio", Time(), nullable=False),
                   Column("regionId", integer(2),
                          ForeingKey(), nullable=False),
                   )

meta_data.bind = engine
meta_data.create_all()
