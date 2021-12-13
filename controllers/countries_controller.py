from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

#NEW
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    return render_template("country/new.html", all_countries = countries)

# CREATE
@countries_blueprint.route("/countries",  methods=['POST'])
def create_country():
    name    = request.form['name']
    language = request.form['language']
    visited = request.form['visited']
    country = Country(name, language, visited)
    country_repository.save(country)
    return redirect('/countries')

# # SHOW??
# @countries_blueprint.route("/countries/<id>", methods=['GET'])
# def show_countries(id):
#     country = country_repository.select(id)
#     return render_template('countries/show.html', country = country)

# # EDIT
# # GET '/stadiums/<id>/edit'
# @stadiums_blueprint.route("/stadiums/<id>/edit", methods=['GET'])
# def edit_stadium(id):
#     stadium = stadium_repository.select(id)
#     countries = country_repository.select_all()
#     return render_template('stadiums/edit.html', stadium = stadium, all_countries = countries)

# # UPDATE
# # PUT '/stadiums/<id>'
# @stadiums_blueprint.route("/stadiums/<id>", methods=['POST'])
# def update_stadium(id):
#     name = request.form['name']
#     category = request.form['category']
#     country  = country_repository.select(request.form['country_id'])
#     visited = request.form['visited']
#     stadium = Stadium(name, category, country, visited, id)
#     print(stadium.country.name)
#     stadium_repository.update(stadium)
#     return redirect('/stadiums')

# # DELETE
# # DELETE '/stadiums/<id>'
# @stadiums_blueprint.route("/stadiums/<id>/delete", methods=['POST'])
# def delete_stadium(id):
#     stadium_repository.delete(id)
#     return redirect('/') 