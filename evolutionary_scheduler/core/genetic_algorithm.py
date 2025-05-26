
import random
from core.timetable import Schedule

POPULATION_SIZE = 50
GENERATIONS = 200
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 5

def initialize_population(input_data):
    return [Schedule.random(input_data) for _ in range(POPULATION_SIZE)]

def fitness(schedule):
    return schedule.calculate_fitness()

def tournament_selection(population):
    tournament = random.sample(population, TOURNAMENT_SIZE)
    return max(tournament, key=fitness)

def crossover(parent1, parent2, input_data):
    return Schedule.crossover(parent1, parent2, input_data)

def mutate(schedule, input_data):
    if random.random() < MUTATION_RATE:
        schedule.mutate(input_data)

def evolve_population(population, input_data):
    new_population = []
    while len(new_population) < POPULATION_SIZE:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child = crossover(parent1, parent2, input_data)
        mutate(child, input_data)
        new_population.append(child)
    return new_population

def run_genetic_algorithm(input_data):
    population = initialize_population(input_data)
    best_schedule = None

    for generation in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)
        if best_schedule is None or fitness(population[0]) > fitness(best_schedule):
            best_schedule = population[0]
        print(f"Generation {generation+1}: Best Fitness = {fitness(best_schedule)}")
        population = evolve_population(population, input_data)

    return best_schedule
