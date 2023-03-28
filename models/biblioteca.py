from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import char, Integer, VARCHAR, BLOB
from config.db import meta_data


estudiante = Table("Biblioteca", metadata,
                   Column("id_biblioteca", integer(2),
                          primary_key=True, nullable=False),
                   Column("nombre", VARCHAR(50), nullable=False),
                   Column("ciudad", varchar(30), nullable=False),
                   Column("region", VARCHAR(50), ForeingKey(), nullable=False),
                   )

meta_data.bind = engine
meta_data.create_all()
