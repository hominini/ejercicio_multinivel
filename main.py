import team_member as tm
from datetime import date
import team as team


def main():
    tm_1 = tm.TeamMember('tm_1', None, [])
    tm_2 = tm.TeamMember('tm_2', tm_1, [])
    tm_3 = tm.TeamMember('tm_3', tm_2, [])
    tm_4 = tm.TeamMember('tm_4', tm_2, [])
    tm_5 = tm.TeamMember('tm_5', tm_4, [])
    tm_6 = tm.TeamMember('tm_6', tm_5, [])
    tm_7 = tm.TeamMember('tm_7', tm_5, [])

    # print(tm_1.print_subtree())

    tm_7.sell(5000.00, date.today())
    tm_7.sell(20.00, date.today())
    tm_6.sell(1000.00, date.today())
    tm_6.sell(200.00, date.today())

    myteam = team.Team()
    team_as_dict = myteam.build_team(tm_1)

    # print(tm_7.get_bonds())
    # tm_1.calculate_sales_total(tm_1)
    print(tm_1.get_sales_total())

    # print(myteam.team_dict)

    # tm_cpy = myteam.get_member_by_id('tm_7')

    # print(tm_cpy)
    # print(tm_6.get_sales())
    # print(tm_1.comissions)


if __name__ == '__main__':
    main()
