class Hall:

    def __init__(self, hall_number, hall_constraints= None):
        if hall_constraints is None:
            self.hall_number = hall_number
            self.hall_constraints = []
            self.domain = []
        else:
            self.hall_number = hall_number
            self.hall_constraints = hall_constraints
            self.domain = []

    def add_constraint(self, constraint):
        self.hall_constraints.append(constraint)

    def __repr__(self):
        return f'Hall(hall_number={self.hall_number}, hall_constraints={self.hall_constraints})'
