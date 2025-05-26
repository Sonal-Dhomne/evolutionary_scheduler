import tkinter as tk
from tkinter import ttk

class TimetableViewer:
    def __init__(self, schedule):
        self.schedule = schedule
        self.root = tk.Tk()
        self.root.title("Generated Timetable Viewer")
        self.tree = None
        self.init_gui()

    def init_gui(self):
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("Course", "Professor", "Group", "Room")
        self.tree.heading("#0", text="Timeslot")
        self.tree.column("#0", anchor=tk.W, width=150)
        
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.W, width=150)
        
        # Group entries by timeslot
        timeslot_map = {}
        for entry in self.schedule.entries:
            ts = entry.timeslot
            if ts not in timeslot_map:
                timeslot_map[ts] = []
            timeslot_map[ts].append(entry)

        # Insert entries into the GUI tree
        for timeslot, entries in sorted(timeslot_map.items()):
            parent = self.tree.insert("", "end", text=timeslot)
            for entry in entries:
                self.tree.insert(
                    parent, "end", text="", 
                    values=(
                        entry.course["name"],
                        entry.course["professor"],
                        entry.course["group"],
                        entry.room["name"]
                    )
                )

        self.tree.pack(expand=True, fill="both")
        self.root.geometry("800x600")

    def run(self):
        self.root.mainloop()

# Usage (example):
# from timetable import Schedule
# import json
# with open("input.json") as f:
#     input_data = json.load(f)
# schedule = Schedule(input_data)  # or best schedule from GA
# viewer = TimetableViewer(schedule)
# viewer.run()
