import json
from core.genetic_algorithm import run_genetic_algorithm
from gui.viewer import TimetableViewer

def load_input(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def main():
    input_path = "data/input.json"
    input_data = load_input(input_path)

    print("Running Genetic Algorithm...")
    best_schedule = run_genetic_algorithm(input_data)

    print("Displaying Timetable...")
    viewer = TimetableViewer(best_schedule)
    viewer.run()

if __name__ == "__main__":
    main()
