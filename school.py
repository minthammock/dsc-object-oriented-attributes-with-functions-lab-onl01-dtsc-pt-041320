class School:
  def __init__(self, name, roster = {}):
    self.name = name
    self.roster = roster
    
  def add_student(self, fullName, gradeLevel):
    if len(self.roster.get(str(gradeLevel),[])) == 0:
      self.roster[str(gradeLevel)] = [fullName]
    else:
      self.roster[str(gradeLevel)].append(fullName)
  def grade(self, gradeLevel):
    return self.roster[str(gradeLevel)]
  def sort_roster(self):
    for x in self.roster.keys():
      self.roster[x].sort()
    print(self.roster)
