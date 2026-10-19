class School:
    def __init__(self):
        self.roster_list = []
        self.added_list = []
        self.grade_list = dict()

    def add_student(self, name, grade):
        if name not in self.roster_list:
            self.added_list.append(True)
            if grade not in self.grade_list.keys():
                self.grade_list[grade] = [name]
                self.grade_list = {k: v for k, v in sorted(self.grade_list.items())}
            else:
                self.grade_list[grade].append(name)
                self.grade_list[grade].sort()
            self.roster_list = []
            for g in self.grade_list.values():
                self.roster_list.extend(g)
        else:
            self.added_list.append(False)

    def roster(self):
        return self.roster_list

    def grade(self, grade_number):
        try:
            return self.grade_list[grade_number]
        except:
            return []

    def added(self):
        return self.added_list
