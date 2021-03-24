from db.run_sql import run_sql
from models.fitness_class import FitnessClass
from models.member import Member

import repositories.trainer_repo as trainer_repo
import repositories.location_repo as location_repo

def save(fitness_class):
    sql = """
    INSERT INTO fitness_classes (title, trainer_id, location_id, date, time, capacity) 
    VALUES ( %s, %s, %s, %s, %s, %s) RETURNING id
    """
    values = [fitness_class.title, fitness_class.trainer.id, fitness_class.location.id, 
    fitness_class.date, fitness_class.time, fitness_class.capacity]
    results = run_sql(sql, values)
    fitness_class.id = results[0]['id']
    return fitness_class

def select_all():
    fitness_classes = []
    sql = "SELECT * FROM fitness_classes ORDER BY date ASC, time ASC"
    results = run_sql(sql)

    for row in results:
        trainer = trainer_repo.select(row['trainer_id'])
        location = location_repo.select(row['location_id'])
        fitness_class = FitnessClass(row['title'], trainer, location, row['date'], row['time'], row['capacity'], row['id'])
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
        fitness_class = FitnessClass(result['title'], trainer, location, result['date'], result['time'], result['capacity'], result['id'])
    return fitness_class

def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fitness_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(fitness_class):
    sql = """
    UPDATE fitness_classes SET (title, trainer_id, location_id, date, time, capacity) 
    = ( %s, %s, %s, %s, %s, %s)
    WHERE id = %s
    """
    values = [fitness_class.title, fitness_class.trainer.id, fitness_class.location.id, 
    fitness_class.date, fitness_class.time, fitness_class.capacity, fitness_class.id]
    run_sql(sql, values)
    
def members(fitness_class):
    values = [fitness_class.id]
    sql = """
        SELECT members.* FROM members 
        INNER JOIN attendance 
        ON members.id = attendance.member_id
        WHERE fitness_class_id = %s
    """
    results = run_sql(sql, values)

    members = []
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['membership'], 
        row['join_date'], row['post_code'], row['phone_number'], row['email'], row['id'])
        members.append(member)
    return members
    
# return members that don't exist in the attendance table for a given fitness class id
def not_members(fitness_class):
    sql = """
        SELECT members.* FROM members
        WHERE NOT EXISTS (
	    SELECT FROM attendance
	    WHERE members.id = attendance.member_id
	    AND attendance.fitness_class_id = %s)
    """
    values = [fitness_class.id]
    results = run_sql( sql, values )

    members = []
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['membership'], 
        row['join_date'], row['post_code'], row['phone_number'], row['email'], row['id'])
        members.append(member)
    return members

def not_members_premium(fitness_class):
    sql = """
        SELECT members.* FROM members
        WHERE NOT EXISTS (
	    SELECT FROM attendance
	    WHERE members.id = attendance.member_id
	    AND attendance.fitness_class_id = %s)
        AND members.membership = 'premium'
    """
    values = [fitness_class.id]
    results = run_sql( sql, values )

    members = []
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['membership'], 
        row['join_date'], row['post_code'], row['phone_number'], row['email'], row['id'])
        members.append(member)
    return members