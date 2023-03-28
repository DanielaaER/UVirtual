from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB, DateTime, Time
from config.db import meta_data


estudiante = Table("visitas_biblioteca", metadata,
                   Column("id_visita", Integer(4),
                          primary_key=True, nullable=False),
                   Column("dia", DateTime(), nullable=False),
                   Column("hora_inicio", Time(), nullable=False),
                   Column("hora_salida", Time(), nullable=False),
                   Column("estudianteMatricula", varchar(10),
                          ForeingKey(), nullable=False),
                   Column("bibliotecaId", integer(2),
                          ForeingKey(), nullable=False),
                   )

meta_data.bind = engine
meta_data.create_all()