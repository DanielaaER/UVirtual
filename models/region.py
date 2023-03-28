from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB, DateTime, Time
from config.db import meta_data


estudiante = Table("region", metadata,
                   Column("id_region", Integer(4),
                          primary_key=True, nullable=False),
                   Column("nombre", VARCHAR(50), nullable=False),
                    )

meta_data.bind = engine
meta_data.create_all()