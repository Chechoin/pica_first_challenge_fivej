# FastAPI Microservice

## Setup

1. **Clone the repository:**
```sh
git clone git@github.com:Chechoin/pica_first_challenge_fivej.git
cd pica_first_challenge_fivej

```

2. **Create a .env file in the root directory:**
```sh
    MYSQL_ROOT_PASSWORD=
    MYSQL_DATABASE=
    MYSQL_USER=
    MYSQL_PASSWORD=
    MYSQL_TCP_PORT=
    MYSQL_HOST=
    USER_CRUD_PORT_INTERNAL=
    USER_CRUD_PORT_EXTERNAL=
    DB_PORT_INTERNAL=
    DB_PORT_EXTERNAL=
    LOG_LEVEL=
    LOG_FORMAT=
```
3. **LOG_LEVEL and when it is used:**
```sh
DEBUG: Detailed information, typically of interest only when diagnosing problems.

INFO: Confirmation that things are working as expected.

WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

ERROR: Due to a more serious problem, the software has not been able to perform some function.

CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
```
4. **Build and run the Docker container:**
```sh
    docker compose down;
    docker compose up --build -d;
    docker compose logs -f --tail 100;
```
5. **Change owner to avoid permissions errors**
```sh
    sudo chown -R $(whoami):$(whoami) mysql_data/
```
6. **main commands to manage ORM:**
migration generation:
```sh
docker compose exec user_crud alembic revision --autogenerate -m "Add hashed_password to User model"
```
run migrations:
```sh
docker compose exec user_crud alembic upgrade head
```
see history migrations
```sh
docker-compose exec user_crud alembic history
```
revert 1 migration
```sh
docker-compose exec user_crud alembic downgrade -1
```
7. **Access the API documentation: Open your browser and go to http://localhost:{USER_CRUD_PORT_EXTERNAL}/docs to see the interactive API documentation.**

### Explanation
- **Database Configuration:** The connection string is managed using environment variables.
- **Database Schema:** The `User` model is defined in `models.py`.
- **API Endpoints:** Implemented in `main.py` with POST, PUT and GET methods.
- **Error Handling:** Basic error handling is included in the `read_user` endpoint.
- **Logging:** You can add logging configurations as needed.
- **Docker:** The `Dockerfile` is provided to build and run the microservice.
- **Dependencies:** Listed in `requirements.txt`.

Feel free to ask if you need any further customization or explanation!
