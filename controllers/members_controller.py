from flask import Flask, Blueprint, render_template, request, redirect
from models.member import Member
from datetime import datetime
import repositories.member_repo as member_repo

members_blueprint = Blueprint('members', __name__)

# show all members
@members_blueprint.route('/members', methods=['GET'])
def index():
    members = member_repo.select_all()
    return render_template('/members/index.html', all_members=members)

# show selected member with all classes they are attending
@members_blueprint.route('/members/<id>', methods=['GET'])
def show(id):
    found_member = member_repo.select(id)
    found_fitness_classes = member_repo.fitness_classes(found_member)
    return render_template('/members/show.html', member=found_member, fitness_classes=found_fitness_classes)

# create a new member form
@members_blueprint.route('/members/new', methods=['GET'])
def new_member():
    return render_template('/members/new.html')

# use info from the create new member form and add to the db
@members_blueprint.route('/members', methods=['POST'])
def create_member():
    date = datetime.today().strftime('%Y-%m-%d')
    member = Member(
        request.form['first_name'], 
        request.form['last_name'], 
        request.form['membership'], 
        date, 
        request.form['post_code'], 
        request.form['phone_number'], 
        request.form['email']
    )
    member_repo.save(member)
    return redirect('/members')

# delete current member
@members_blueprint.route('/members/<id>/delete', methods=['POST'])
def delete_member(id):
    member_repo.delete(id)
    return redirect('/members')
    