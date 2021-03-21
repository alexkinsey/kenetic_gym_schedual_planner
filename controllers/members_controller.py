from flask import Flask, Blueprint, render_template, request, redirect
from models.member import Member
import repositories.member_repo as member_repo

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members', methods=["GET"])
def index():
    members = member_repo.select_all()
    return render_template('/members/index.html', all_members=members)