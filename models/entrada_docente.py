from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB, DateTime, Time
from config.db import meta_data


estudiante = Table("entrada_docente", metadata,
                   Column("id_entradaDocente", Integer(4),
                          primary_key=True, nullable=False),
                   Column("dia", DateTime(), nullable=False),
                   Column("hora_inicio", Time(), nullable=False),
                   Column("docente_id", varchar(10),
                          ForeingKey(), nullable=False),
                   Column("Clase_id", integer(4),
                          ForeingKey(), nullable=False),
                   )

meta_data.bind = engine
meta_data.create_all()