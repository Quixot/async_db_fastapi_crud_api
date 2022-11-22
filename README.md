pip install fastapi sqlalchemy[asyncio] uvicorn[standard] alembic aiosqlite

**git** init  
**git** add .  
**git** commit -m "Basic structure"  
**git** remote add origin https://github.com/<addres_to_repo>  
**git** push -u origin master

**alembic** init -t **async** alembic
alembic.ini
...  
sqlalchemy.url = sqlite:///./database.db  

env.py  
...  
from database import Base  
import models  
target_metadata = Base.metadata  

**alembic** revision --autogenerate -m "First Revision"
**alembic** upgrade head  
**alembic** upgrade 123
