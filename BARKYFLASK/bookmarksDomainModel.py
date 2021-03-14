from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class bookmarksDomainModel(Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique = True, nullable=False)
    url = Column(String(50), unique = True, nullable=False)
    notes = Column(String(50), unique = True, nullable=False)
    date_added = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name