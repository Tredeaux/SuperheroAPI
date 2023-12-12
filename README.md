# Superhero API
### This is an API for searching Superhero's
 
> Run
> > docker-compose up --build



> To Build Migrations
> > flask db upgrade


## Endpoints
### Init [GET]

> http://localhost:5000/init

### Search [POST]

> http://localhost:5000/superhero
>  ```json
> { 
> 'superhero': "<Superhero name here>", 
> }
>  ```

