class BuildingEror(Exception):
   def __str__(self):
    return "netu materialov slishkom mala ne moshno stroit"
def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "dostatochno materialov"
    else:
        raise BuildingEror(amount_of_material)
materials = 123
check_material(materials, 300)
