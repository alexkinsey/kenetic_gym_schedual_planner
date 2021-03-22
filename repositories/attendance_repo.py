from db.run_sql import run_sql
from models.attendance import Attendance

import repositories.member_repo as member_repo
import repositories.fitness_class_repo as fitness_class_repo

def save(attendance):
    sql = """
    INSERT INTO attendance (fitness_class_id, member_id) 
    VALUES ( %s, %s ) RETURNING id
    """
    values = [attendance.fitness_class.id, attendance.member.id]
    results = run_sql(sql, values)
    attendance.id = results[0]['id']
    return attendance

def select_all():
    attendance_list = []
    sql = "SELECT * FROM attendance"
    results = run_sql(sql)

    for row in results:
        member = member_repo.select(row['member_id'])
        fitness_class = fitness_class_repo.select(row['fitness_class_id'])
        attendance = Attendance(fitness_class, member, row['id'])
        attendance_list.append(attendance)
    return attendance_list

def select(id):
    attendance = None
    sql = "SELECT * FROM attendance WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = member_repo.select(result['member_id'])
        fitness_class = fitness_class_repo.select(result['fitness_class_id'])
        attendance = Attendance(fitness_class, member, result['id'])
    return attendance

def delete_all():
    sql = "DELETE FROM attendance"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM attendance WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_by_fitness_class_and_member(fitness_class, member):
    sql = "DELETE FROM attendance WHERE fitness_class_id = %s AND member_id = %s"
    values = [fitness_class.id, member.id]
    run_sql(sql, values)

def update(attendance):
    sql = """
    UPDATE attendance SET (fitness_class_id, member_id) = ( %s, %s ) 
    WHERE id = %s
    """
    values = [attendance.fitness_class.id, attendance.member.id, attendance.id]
    results = run_sql(sql, values)
    