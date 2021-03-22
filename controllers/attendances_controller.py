from flask import Flask, Blueprint, render_template, request, redirect
from models.fitness_class import FitnessClass
import repositories.fitness_class_repo as fitness_class_repo
import repositories.member_repo as member_repo

attendances_blueprint = Blueprint('attendances', __name__)

@attendances_blueprint.route('/attendances/new/<id>', methods=['GET'])
def sign_up_member(id):
    found_fitness_class = fitness_class_repo.select(id)
    all_members = member_repo.select_all()
    return render_template('/attendance/new.html', fitness_class=found_fitness_class, members=all_members)