from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the Base class for ORM models to inherit from
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'  # Define the table name in the database

    # Define columns for the table
    id = Column(Integer, primary_key=True)
    name = Column(String)

# If the script is executed directly, create the database and table
if __name__ == '__main__':
    # Create an engine that stores data in a local SQLite database
    engine = create_engine('sqlite:///students.db')

    # Create all tables in the database, based on Base metadata
    Base.metadata.create_all(engine)
