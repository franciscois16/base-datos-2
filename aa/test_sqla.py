from datetime import datetime
from sqlalchemy import ForeignKey, String, create_engine, select, update
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
 
 
class Base(DeclarativeBase):
    pass
 
 
class User(Base):
    __tablename__ = "users"
 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    is_enabled: Mapped[bool] = mapped_column(
        default=True, server_default="1", nullable=False
    )
    origin_id: Mapped[int] = mapped_column(
        ForeignKey("origins.id", ondelete="SET NULL"), nullable=True
    )
    password: Mapped[str] = mapped_column(String(128), nullable=True)
    last_login: Mapped[datetime] = mapped_column(nullable=False)
    origin: Mapped["Origin"] = relationship(back_populates="users")
 
    items: Mapped[list["Item"]] = relationship(
        back_populates="users", secondary="user_items"
    )
    
    groups: Mapped[list["Group"]] = relationship(
        back_populates="users", secondary="user_group"
    )
 
    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', is_enabled={self.is_enabled})"
    
class Group(Base):
    __tablename__ = "groups"
 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    is_enabled: Mapped[bool] = mapped_column(
        default=True, server_default="1", nullable=False
    )
    
    users: Mapped[list["User"]] = relationship(
        back_populates="groups", secondary="user_group"
    )
 
    def __repr__(self) -> str:
        return f"Group(id={self.id}, name='{self.name}', is_enabled={self.is_enabled})"
    
class UserGroup(Base):
    __tablename__ = "user_group"
 
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), primary_key=True)
 
 
class Origin(Base):
    __tablename__ = "origins"
 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(64), nullable=False, index=True, unique=True
    )
 
    users: Mapped[list["User"]] = relationship(back_populates="origin")
 
    def __repr__(self) -> str:
        return f"Origin(id={self.id}, name='{self.name}')"
 
 
class Item(Base):
    __tablename__ = "items"
 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(64), nullable=False, index=True, unique=True
    )
 
    users: Mapped[list["User"]] = relationship(
        back_populates="items", secondary="user_items"
    )
    
    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id", ondelete="SET NULL"), nullable=True
    )
        
    category: Mapped["Category"] = relationship(back_populates="items")
 
class UserItem(Base):
    __tablename__ = "user_items"
 
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), primary_key=True)
    # quantity: Mapped[int]
 
    # user: Mapped["User"] = relationship(back_populates="items")
    # item: Mapped["Item"] = relationship(back_populates="users")
 
class Category(Base):
    __tablename__ = "category"
 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(64), nullable=False, index=True, unique=True
    )
 
    items: Mapped[list["Item"]] = relationship(back_populates="category")
 
    def __repr__(self) -> str:
        return f"Category(id={self.id}, name='{self.name}')"
 
engine = create_engine("postgresql+psycopg:///test", echo=False)
Base.metadata.create_all(engine)
 
with Session(engine) as session:
    # añadir orígenes
    o1 = Origin(name="interno")
    o2 = Origin(name="externo")
    session.add_all([o1, o2])
 
    uu = [
        User(name="Miguel", last_login=datetime.now()),
        User(name="Javiera", last_login=datetime.now()),
        User(name="Catalina", last_login=datetime.now()),
    ]
    session.add_all(uu)
 
    o1.users = uu
 
    ii = [Item(name="lápiz"), Item(name="mouse"), Item(name="cable")]
 
    uu[0].items = [ii[0], ii[1]]
    g1 = Group(name="grupo1")
    g1.users = [uu[0]]
    session.add(g1)
 
    # ui = [UserItem(user=uu[0], item=ii[0]), UserItem(user=uu[1], item=ii[2])]
    # uu[0].items = [
    #     UserItem(item=ii[1]),
    #     UserItem(item=ii[2])
    # ]
    # session.add_all(uu)
 
    # añadir usuarios
    # session.add_all(
    #     [
    #         User(name="Miguel", origin=o1),
    #         User(name="Javiera", origin=o2),
    #         User(name="Catalina", origin=o1),
    #     ]
    # )
    session.commit()
 
    # consulta
    smt = select(User).filter_by(name="Javiera")
    javiera = session.execute(smt).scalar_one()
 
    print(javiera.origin.name)
 
    # consulta
    smt2 = select(Origin)
    o1 = session.execute(smt2).scalars().first()
    if o1 is not None:
        for user in o1.users:
            print(user.name)
 
    session.commit()
 
    # # actualizar un objeto
    # smt = select(User).where(User.id==1)#.order_by(User.id.desc())
    # diego = session.execute(smt).scalar_one()
    # diego.is_enabled = False
 
    # # actualización masiva
    # smt_up = update(User).where(User.name == "Diego").values(is_enabled=False)
    # session.execute(smt_up)
 
    # session.commit()
    
#Agrager una tabla "Category", y cada item puede tener una categoria (o no)
#Agregar el campo 'password' (str puede ser null) y last_login (datetime, no nulo) a user
#Añadir la tabla "Group", que debe tener relacion N:N con usuarios