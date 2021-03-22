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
    all_members = member_repo.select_all()
    return render_template('/attendances/new.html', fitness_class=found_fitness_class, members=all_members)

# commit member to fitness class in db
@attendances_blueprint.route('/attendances', methods=['POST'])
def update():
    found_member = member_repo.select(request.form['member_id'])
    found_fitness_class = fitness_class_repo.select(request.form['fitness_class_id'])
    attendance = Attendance(found_fitness_class, found_member)

    attendance_repo.save(attendance)
    return redirect('/classes')