from flask import Blueprint, redirect, render_template, request, url_for
import requests
import json

crud = Blueprint('crud', __name__)


@crud.route("/")
def main():
    r = requests.get("http://localhost:5000")
    #return r.json()['hello']
    return render_template("main.html", request=r.json()['hello'])


# Sample code for referenece
# @crud.route('/<id>/edit', methods=['GET', 'POST'])
# def edit(id):
#     book = get_model().read(id)
    
#     if request.method == 'POST':
#         data = request.form.to_dict(flat=True)

#         book = get_model().update(data, id)

#         return redirect(url_for('.view', id=book['id']))
    
#     return render_template("form.html", action="Edit", book=book)
