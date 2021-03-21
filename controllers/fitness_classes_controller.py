from flask import Flask, Blueprint, render_template, request, redirect
from models.fitness_class import FitnessClass
import repositories.fitness_class_repo as fitness_class_repo

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
