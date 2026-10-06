from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Musica(Base):
    __tablename__ = "tabela_Musica"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    genero: Mapped[str] = mapped_column(String(50))
    duracao: Mapped[str] = mapped_column(String(50))
    ano_lancamento: Mapped[int] = mapped_column(Integer)

class Cantor(Base):
    __tablename__ = "tabela_Cantor"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    ano_inicio_carreira: Mapped[int] = mapped_column(Integer)
    genero_musical: Mapped[str] = mapped_column(String(50))
    pais_origem: Mapped[str] = mapped_column(String(55))

engine = create_engine("mysql+pymysql://root:@localhost:3306/meubanco")

Base.metadata.create_all(engine)
