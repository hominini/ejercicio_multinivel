from flask import Flask, render_template
app = Flask(__name__)

from team_member import TeamMember
from team import Team
from datetime import date
import sys
import json

# datos iniciales de prueba, no alcance a hacer que consuma de algun archivo
# pero con un poco mas de tiempo hubiera hecho que ingrese por un formulario
# o que lea de una base de datos
'''
            tm_1
              |
            tm_2
            /  \
          tm_3 tm_4
                 |
               tm_5
               /  \
             tm_6 tm_7

'''
tm_1 = TeamMember('tm_1', None, [])
tm_2 = TeamMember('tm_2', tm_1, [])
tm_3 = TeamMember('tm_3', tm_2, [])
tm_4 = TeamMember('tm_4', tm_2, [])
tm_5 = TeamMember('tm_5', tm_4, [])
tm_6 = TeamMember('tm_6', tm_5, [])
tm_7 = TeamMember('tm_7', tm_5, [])

# el nodo 7 vende 5000
tm_7.sell(5000.00, date.today())
# el nodo 7 vende 5000
tm_7.sell(20.00, date.today())
# el nodo 6 vende 25000
tm_6.sell(25000.00, date.today())
# el nodo 6 vende 200
tm_6.sell(200.00, date.today())


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", team = [tm_1])

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/team_member/<id>")
def team_member(id):
    team_member = {}
    myteam = Team()
    myteam.build_team(tm_1)
    tm = myteam.get_member_by_id(id)
    team_member['id'] = tm.id
    team_member['ventas'] = [e.__str__() for e in tm.get_sales()]
    team_member['comisiones'] = [e.__str__() for e in tm.get_comissions()]
    team_member['bonos'] = tm.get_bonds()
    return json.dumps(team_member)

@app.route("/team/<leader_id>/total_sales")
def get_total_sales_of_team(leader_id):
    team_sales = 0.0
    myteam = Team()
    myteam.build_team(tm_1)
    tm = myteam.get_member_by_id(leader_id)
    team_sales = tm.get_sales_total()
    return json.dumps({'team_sales': team_sales})


if __name__ == '__main__':
    app.run(debug=True)