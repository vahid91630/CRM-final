from .models import Base
from .session import engine

# Auto create all tables when package is imported
Base.metadata.create_all(bind=engine)
