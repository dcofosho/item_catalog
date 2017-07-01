import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
	__tablename__ = "user"
	name = Column(
		String(80), nullable = False)
	email = Column(
		String(80), nullable = True)
	picture = Column(
		String(80), nullable = True)
	id = Column(
		Integer, primary_key = True)

	@property
	def serialize(self):
		#Return object data in easily serializeable format
		return {
        	'name': self.name,
        	'email': self.email,
        	'picture': self.picture,
        	'id': self.id,
    	}


class Category(Base):
	__tablename__ = "category"
	name = Column(
		String(80), nullable = False)
	user_id = Column(
		Integer, ForeignKey('user.id'))
	id = Column(
		Integer, primary_key = True)
	user = relationship(User)

	@property
	def serialize(self):
		#Return object data in easily serializeable format
		return {
        	'name': self.name,
        	'user_id': self.user_id,
        	'id': self.id,
    	}

class Item(Base):
	__tablename__ = 'item'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	price = Column(String(8))

	category_id = Column(
		Integer, ForeignKey('category.id'))
	user_id = Column(
		Integer, ForeignKey('user.id'))

	category = relationship(Category)
	user = relationship(User)

	@property
	def serialize(self):
		# returns object data in easily serializable format
		return{
			'name': self.name,
			'description': self.description,
			'category_id': self.category_id,
			'user_id': self.user_id,
			'id': self.id,
			'price': self.price,
		}


######INSERT AT END OF FILE#####

engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)