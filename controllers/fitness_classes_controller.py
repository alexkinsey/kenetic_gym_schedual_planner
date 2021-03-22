from flask import Flask, Blueprint, render_template, request, redirect
from models.fitness_class import FitnessClass
import repositories.fitness_class_repo as fitness_class_repo
import repositories.trainer_repo as trainer_repo
import repositories.location_repo as location_repo

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
    return render_template('/fitness_classes/show.html', members=found_members, fitness_class=found_fitness_class)

@fitness_classes_blueprint.route('/classes/new', methods=['GET'])
def new_fitness_class():
    all_trainers = trainer_repo.select_all()
    all_locations = location_repo.select_all()
    return render_template('/fitness_classes/new.html', trainers=all_trainers, locations=all_locations)