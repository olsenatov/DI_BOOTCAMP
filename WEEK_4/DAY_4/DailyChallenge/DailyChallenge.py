import requests
import random
import psycopg2

# API request
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
countries_data = response.json()

# random list of 10 countries
random_countries = random.sample(countries_data, 10)

# database
connection = psycopg2.connect(
    dbname="DailyChallenge_d4",
    user='postgres',
    password='veampti0312',
    host='localhost',
    port='5432'
)
cursor = connection.cursor()

# create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        name TEXT,
        capital TEXT,
        population INTEGER
    )
""")

#put random countries to list
for country in random_countries:
    name = country['name']['common']
    capital = country.get('capital', 'N/A')
    population = country.get('population', 0)

    cursor.execute('INSERT INTO countries VALUES (%s, %s, %s)', (name, capital, population))

connection.commit()
connection.close()
