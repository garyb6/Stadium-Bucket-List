from db.run_sql import run_sql

from models.stadium import Stadium
import repositories.country_repository as country_repository 

def save(stadium):
    sql = "INSERT INTO stadiums (name, category, description, city, country_id, visited, rating) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [stadium.name, stadium.category, stadium.description, stadium.city, stadium.country.id, stadium.visited, stadium.rating]
    results = run_sql(sql, values)
    id = results[0]['id']
    stadium.id = id 
    return stadium 

def select_all():
    stadiums = []
    sql = "SELECT * FROM stadiums"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        stadium = Stadium(row['name'], row['category'], row['description'], row['city'], country, row['visited'], row['rating'], row['id'])
        stadiums.append(stadium)
    return stadiums 

def select(id):
    stadium = None
    sql = "SELECT * FROM stadiums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repository.select(result['country_id'])
        stadium = Stadium(result['name'], result['category'], result['description'], result['city'], country, result['visited'], result['rating'], result['id'])
    return stadium 

def delete_all():
    sql = "DELETE FROM stadiums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM stadiums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(stadium):
    sql = "UPDATE stadiums SET (name, category, description, city, country_id, visited, rating) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [stadium.name, stadium.category, stadium.description, stadium.city, stadium.country.id, stadium.visited, stadium.rating, stadium.id]
    run_sql(sql, values)

def select_visited():
    stadiums = []
    sql = "SELECT * FROM stadiums WHERE visited = 'TRUE'"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        stadium = Stadium(row['name'], row['category'], row['description'], row['city'], country, row['visited'], row['rating'], row['id'])
        stadiums.append(stadium)
    return stadiums 

def select_to_visit():
    stadiums = []
    sql = "SELECT * FROM stadiums WHERE visited = 'FALSE'"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        stadium = Stadium(row['name'], row['category'], row['description'], row['city'], country, row['visited'], row['rating'], row['id'])
        stadiums.append(stadium)
    return stadiums 