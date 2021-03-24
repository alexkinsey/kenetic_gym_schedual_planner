from flask import Flask, Blueprint, render_template, request, redirect
from models.attendance import Attendance
import repositories.fitness_class_repo as fitness_class_repo
import repositories.member_repo as member_repo
import repositories.attendance_repo as attendance_repo

attendances_blueprint = Blueprint('attendances', __name__)

# triggered from fitness class show page
# form to add member to a class
@attendances_blueprint.route('/attendances/new/<id>', methods=['GET'])
def sign_up_member_form(id):
    found_fitness_class = fitness_class_repo.select(id)
    if (found_fitness_class.time.hour >= 17 and found_fitness_class.time.hour <19) or (found_fitness_class.time.hour >= 7 and found_fitness_class.time.hour <9):
        not_attending = fitness_class_repo.not_members_premium(found_fitness_class)
    else:
        not_attending = fitness_class_repo.not_members(found_fitness_class)
    return render_template('/attendances/new.html', fitness_class=found_fitness_class, members=not_attending)
   

# commit member to fitness class in db
@attendances_blueprint.route('/attendances', methods=['POST'])
def update():
    found_member = member_repo.select(request.form['member_id'])
    found_fitness_class = fitness_class_repo.select(request.form['fitness_class_id'])
    # verify there is availability on the class if for some reason the user manages to get this far
    calc_availability = found_fitness_class.capacity - len(attendance_repo.select_by_fitness_class(found_fitness_class))
    if calc_availability > 0:
        attendance = Attendance(found_fitness_class, found_member)
        attendance_repo.save(attendance)
    else:
        return render_template('/errors/405.html'), 405
    return redirect('/classes/' + str(found_fitness_class.id))

# delete member from fitness class
# <id> is customer id
@attendances_blueprint.route('/attendances/<id>/delete', methods=['POST'])
def delete(id):
    member = member_repo.select(request.form['member_id'])
    fitness_class = fitness_class_repo.select(request.form['fitness_class_id'])
    attendance_repo.delete_by_fitness_class_and_member(fitness_class, member)
    return redirect('/classes/' + str(fitness_class.id))
