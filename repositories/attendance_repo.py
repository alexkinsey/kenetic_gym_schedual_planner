from db.run_sql import run_sql
from models.attendance import Attendance

import repositories.customer_repo as customer_repo
import repositories.fitness_class_repo as fitness_class_repo

def save(attendance):
    sql = """INSERT INTO attendance (fitness_class_id, customer_id) 
    VALUES ( %s, %s ) RETURNING id
    """
    values = [attendance.fitness_class.id, attendance.customer.id]
    results = run_sql(sql, values)
    attendance.id = results[0]['id']
    return attendance

def select_all():
    attendance_list = []
    sql = "SELECT * FROM attendance"
    results = run_sql(sql)

    for row in results:
        customer = customer_repo.select(row['customer_id'])
        fitness_class = fitness_class_repo.select(row['fitness_class_id'])
        attendance = Attendance(fitness_class, customer, row['id'])
        attendance_list.append(attendance)
    return attendance_list

def select(id):
    attendance = None
    sql = "SELECT * FROM attendance WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        customer = customer_repo.select(result['customer_id'])
        fitness_class = fitness_class_repo.select(result['fitness_class_id'])
        attendance = Attendance(fitness_class, customer, result['id'])
    return attendance

def delete_all():
    sql = "DELETE FROM attendance"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM attendance WHERE id = %s"
    values = [id]
    run_sql(sql, values)