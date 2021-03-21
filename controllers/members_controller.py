from flask import Flask, Blueprint, render_template, request, redirect
from models.member import Member
import repositories.member_repo as member_repo

members_blueprint = Blueprint('members', __name__)

# show all members
@members_blueprint.route('/members', methods=['GET'])
def index():
    members = member_repo.select_all()
    return render_template('/members/index.html', all_members=members)

# show selected member
@members_blueprint.route('/members/<id>', methods=['GET'])
def show(id):
    found_member = member_repo.select(id)
    found_fitness_classes = member_repo.fitness_classes(found_member)
    return render_template('/members/show.html', member=found_member, fitness_classes=found_fitness_classes)