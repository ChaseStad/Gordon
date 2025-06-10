class UnitManager:
    def __init__(self):
        self.roles = {}  # unit.tag -> role

    def assign_role(self, unit, role):
        self.roles[unit.tag] = role
    
    def get_role(self, unit):
        return self.roles.get(unit.tag, "nothing")

    def count_role(self,role):
        return list(self.roles.values()).count(role)

    def remove_dead_units(self, alive_units):
        alive_tags = {u.tag for u in alive_units}
        self.roles = {tag: role for tag, role in self.roles.items() if tag in alive_tags}

    def get_units_by_role(self,all_units,role):
        return [unit for unit in all_units if self.get_role(unit) == role]
        