class Team:

    team_dict = {}

    def __init__(self):
        self.team = self.team_dict

    def add_member(self, member):
        pass

    def get_member_by_id(self, id):
        if id in self.team_dict:
            return self.team_dict[id]
        else:
            return None

    @classmethod
    def build_team(self, team_root):
        self.team_dict[team_root.id] = team_root
        for child in team_root.child_members:
            self.build_team(child)

    