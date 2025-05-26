import random
import copy

class TimetableEntry:
    def __init__(self, course, room, timeslot):
        self.course = course
        self.room = room
        self.timeslot = timeslot

class Schedule:
    def __init__(self, input_data):
        self.input_data = input_data
        self.entries = []
        self.fitness_score = None
        self.generate_random_schedule()

    def generate_random_schedule(self):
        self.entries = []
        for course in self.input_data['courses']:
            room = random.choice(self.input_data['rooms'])
            timeslot = random.choice(self.input_data['timeslots'])
            entry = TimetableEntry(course, room, timeslot)
            self.entries.append(entry)

    @staticmethod
    def random(input_data):
        return Schedule(input_data)

    @staticmethod
    def crossover(parent1, parent2, input_data):
        child = Schedule(input_data)
        for i in range(len(parent1.entries)):
            if random.random() > 0.5:
                child.entries[i] = copy.deepcopy(parent1.entries[i])
            else:
                child.entries[i] = copy.deepcopy(parent2.entries[i])
        return child

    def mutate(self, input_data):
        idx = random.randint(0, len(self.entries) - 1)
        self.entries[idx].room = random.choice(input_data['rooms'])
        self.entries[idx].timeslot = random.choice(input_data['timeslots'])

    def calculate_fitness(self):
        conflicts = 0
        seen = {}

        for i, entry in enumerate(self.entries):
            key = (entry.timeslot, entry.room['name'])
            if key in seen:
                conflicts += 1
            else:
                seen[key] = i

            # Room capacity constraint
            group = next(g for g in self.input_data['student_groups'] if g['name'] == entry.course['group'])
            if entry.room['capacity'] < group['size']:
                conflicts += 1

            # Professor timeslot conflict
            prof_key = (entry.course['professor'], entry.timeslot)
            if prof_key in seen:
                conflicts += 1
            else:
                seen[prof_key] = i

            # Group timeslot conflict
            group_key = (entry.course['group'], entry.timeslot)
            if group_key in seen:
                conflicts += 1
            else:
                seen[group_key] = i

        self.fitness_score = 1 / (1 + conflicts)
        return self.fitness_score
