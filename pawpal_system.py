from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List

@dataclass
class Task:
    title: str
    duration: int  # in minutes
    time: str      # format "HH:MM"
    priority: str  # "high", "medium", "low"
    completed: bool = False

    def mark_complete(self):
        self.completed = True

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

class Scheduler:
    """The 'Brain' that organizes tasks."""
    
    @staticmethod
    def get_sorted_tasks(tasks: List[Task]):
        """Algorithm: Sorts tasks chronologically by time string."""
        return sorted(tasks, key=lambda x: x.time)

    @staticmethod
    def detect_conflicts(tasks: List[Task]):
        """Algorithm: Finds if multiple tasks are scheduled for the same time."""
        time_counts = {}
        for t in tasks:
            time_counts[t.time] = time_counts.get(t.time, 0) + 1
        
        conflicts = [time for time, count in time_counts.items() if count > 1]
        return conflicts

    @staticmethod
    def calculate_total_time(tasks: List[Task]):
        """Algorithm: Sums up the duration of all scheduled tasks."""
        return sum(t.duration for t in tasks)