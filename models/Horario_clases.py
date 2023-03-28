from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB, DateTime, Time
from config.db import meta_data


estudiante = Table("horarioClases", metadata,
                   Column("id_horario", Integer(4),
                          primary_key=True, nullable=False),
                   Column("dia", DateTime(), nullable=False),
                   Column("hora_inicio", Time(), nullable=False),
                   Column("hora_inicio", Time(), nullable=False),
                   Column("nrc", integer(4),
                          ForeingKey(), nullable=False),
                   )

meta_data.bind = engine
meta_data.create_all()
