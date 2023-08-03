import psycopg2

# CONNECT TO THE DATABASE
connection = psycopg2.connect(
    database="hollywood", 
    user='postgres',
    password='veampti0312',
    host='localhost', #or IP address
    port='5432'
)

# def retrieve_actors ():
#     try:
        
#         with connection:
#             with connection.cursor() as curs:
#                 query = "SELECT * FROM actors"
#                 curs.execute(query)
#                 data = curs.fetchall()
#                 print(data)
#                 pass
#        
#     except Exception as err:
#         print(err)
        
# retrieve_actors()


def retrieve_actors (last_name):
    try:
        
        with connection:
            with connection.cursor() as curs:
                query = """
                SELECT first_name, last_name title
                from actors 
                Inner join actors_movies on actors.actor_id = actors_movies.actor_id
                Inner join movie on movie.id = actors_movies.movie_id
                """
                curs.execute(query)
                data = curs.fetchall()
                print(data)
                pass
       
    except Exception as err:
        print(err)
        
retrieve_actors('Cohen')


connection.close()