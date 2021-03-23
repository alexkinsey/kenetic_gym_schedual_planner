from flask import Flask, Blueprint, render_template, request, redirect
from models.fitness_class import FitnessClass
import repositories.fitness_class_repo as fitness_class_repo
import repositories.trainer_repo as trainer_repo
import repositories.location_repo as location_repo
import repositories.attendance_repo as attendance_repo

fitness_classes_blueprint = Blueprint('fitness_classes', __name__)

# show all classes
@fitness_classes_blueprint.route('/classes', methods=['GET'])
def index():
    fitness_classes = fitness_class_repo.select_all()
    return render_template('/fitness_classes/index.html', all_fitness_classes=fitness_classes)

# show selected class with members attending
@fitness_classes_blueprint.route('/classes/<id>', methods=['GET'])
def show(id):
    found_fitness_class = fitness_class_repo.select(id)
    found_members = fitness_class_repo.members(found_fitness_class)
    calc_availability = found_fitness_class.capacity - len(attendance_repo.select_by_fitness_class(found_fitness_class))
    return render_template(
        '/fitness_classes/show.html', 
        members=found_members, 
        fitness_class=found_fitness_class, 
        availability=calc_availability
    )

# create new fitness class form
@fitness_classes_blueprint.route('/classes/new', methods=['GET'])
def new_fitness_class():
    all_trainers = trainer_repo.select_all()
    all_locations = location_repo.select_all()
    return render_template('/fitness_classes/new.html', trainers=all_trainers, locations=all_locations)

# use form data to create new fitness class
@fitness_classes_blueprint.route('/classes', methods=['POST'])
def create_new_fitness():
    trainer = trainer_repo.select(request.form['trainer_id'])
    location = location_repo.select(request.form['location_id'])
    fitness_class = FitnessClass(
        request.form['title'],
        trainer,
        location,
        request.form['date'],
        request.form['time'],
        request.form['capacity']
    )
    fitness_class_repo.save(fitness_class)
    return redirect('/classes')

# edit current fitness class
@fitness_classes_blueprint.route('/classes/<id>/edit', methods=['GET'])
def edit(id):
    found_fitness_class = fitness_class_repo.select(id)
    all_trainers = trainer_repo.select_all()
    all_locations = location_repo.select_all()
    return render_template(
        '/fitness_classes/edit.html', 
        fitness_class=found_fitness_class, 
        trainers=all_trainers, 
        locations=all_locations
    )

# update fitness class db after edits
@fitness_classes_blueprint.route('/classes/<id>', methods=['POST'])
def update(id):
    trainer = trainer_repo.select(request.form['trainer_id'])
    location = location_repo.select(request.form['location_id'])
    fitness_class = FitnessClass(
        request.form['title'],
        trainer,
        location,
        request.form['date'],
        request.form['time'],
        request.form['capacity'],
        id
    )
    fitness_class_repo.update(fitness_class)
    id_str = str(fitness_class.id)
    url = '/classes/' + id_str
    return redirect(url)