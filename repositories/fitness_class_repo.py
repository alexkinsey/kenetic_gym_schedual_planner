from db.run_sql import run_sql
from models.fitness_class import FitnessClass

import repositories.trainer_repo as trainer_repo
import repositories.location_repo as location_repo

def save(fitness_class):
    sql = """INSERT INTO fitness_classes (title, trainer_id, location_id, date, time, capacity) 
        VALUES ( %s, %s, %s, %s, %s, %s) RETURNING id
    """
    values = [fitness_class.title, fitness_class.trainer.id, fitness_class.location.id, 
    fitness_class.date, fitness_class.time, fitness_class.capacity]
    results = run_sql(sql, values)
    fitness_class.id = results[0]['id']
    return fitness_class

def select_all():
    fitness_classes = []
    sql = "SELECT * FROM fitness_classes"
    results = run_sql(sql)

    for row in results:
        trainer = trainer_repo.select(row['trainer_id'])
        location = location_repo.select(row['location_id'])
        fitness_class = FitnessClass(row['title'], trainer, location, row['date'], row['time'], row['capacity'])
        fitness_classes.append(fitness_class)
    return fitness_classes

def select(id):
    fitness_class = None
    sql = "SELECT * FROM fitness_classes WHERE id = %s"
    values = [id]
    result = run_sql( sql, values )[0]

    if result is not None:
        trainer = trainer_repo.select(result['trainer_id'])
        location = location_repo.select(result['location_id'])
        fitness_class = FitnessClass(result['title'], trainer, location, result['date'], result['time'], result['capacity'])
    return fitness_class

def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fitness_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)
