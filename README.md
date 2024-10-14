# This site is for currency conversion on FastAPI

### The tutorial project is designed to convert currency using a third-party API.
### It would also be cool to use Frontend in tandem with Backend


# Docker commands
- https://itsfoss.com/install-docker-arch-linux/
- docker build . -t currency
- Waiting
- docker run -p 8000:8000 currency
- http://127.0.0.1:8000/docs
- docker stop currency
- docker run -it --rm currency /bin/bash  
### If you need to remove all Docker containers (Dangerous, this will remove all images)
- docker system prune -a   

# Alembic 
- alembic init migrations                                                       
- alembic revision --autogenerate -m "Database creation"
- alembic upgrade head   