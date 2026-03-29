"""PawPal+ backend — pet care task scheduling system."""

from __future__ import annotations

from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class Species(Enum):
    """The type of animal a pet is."""
    CAT = "Cat"
    DOG = "Dog"
    OTHER = "Other"


class Priority(Enum):
    """How urgent a task is."""
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Status(Enum):
    """The current state of a task."""
    PENDING = "Pending"
    COMPLETED = "Completed"
    SKIPPED = "Skipped"


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

class Preferences:
    """Stores owner-level notification and scheduling preferences."""

    def __init__(self, reminder_time: str) -> None:
        """
        Args:
            reminder_time: Time string (e.g. "08:00") for daily reminders.
        """
        self.reminder_time = reminder_time


class Pet:
    """Represents a single pet belonging to an owner."""

    def __init__(self, name: str, age: int, breed: str, species: Species) -> None:
        """
        Args:
            name:    Pet's name.
            age:     Pet's age in years.
            breed:   Breed description.
            species: One of the Species enum values.
        """
        self.name = name
        self.age = age
        self.breed = breed
        self.species = species


class Owner:
    """Links a person to their preferences and list of pets."""

    def __init__(
        self,
        name: str,
        preferences: Preferences,
        pets: Optional[list[Pet]] = None,
    ) -> None:
        """
        Args:
            name:        Owner's display name.
            preferences: Notification and scheduling preferences.
            pets:        Initial list of pets (defaults to empty list).
        """
        self.name = name
        self.preferences = preferences
        self.pets: list[Pet] = pets if pets is not None else []
    
    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list of pets."""
        self.pets.append(pet)


class Task:
    """A single schedulable pet-care activity."""

    def __init__(
        self,
        title: str,
        duration_minutes: int,
        priority: Priority,
        pet: Pet,
        time: Optional[datetime] = None,
        status: Status = Status.PENDING,
    ) -> None:
        """
        Args:
            title:            Short description of the task (e.g. "Morning walk").
            duration_minutes: How long the task takes.
            priority:         HIGH, MEDIUM, or LOW.
            pet:              The pet this task is for.
            time:             Scheduled start time; None until the scheduler assigns it.
            status:           Current state; defaults to PENDING.
        """
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.pet = pet
        self.time = time
        self.status = status


class Schedule:
    """A generated daily plan containing an ordered list of tasks and a summary."""

    def __init__(self) -> None:
        self.tasks: list[Task] = []
        self.description: str = ""


# ---------------------------------------------------------------------------
# Service
# ---------------------------------------------------------------------------

class PetCareService:
    """Singleton service that manages tasks and produces schedules."""

    _instance: Optional[PetCareService] = None

    def __init__(self) -> None:
        self._tasks: list[Task] = []

    # ------------------------------------------------------------------
    # Singleton access
    # ------------------------------------------------------------------

    @classmethod
    def get_instance(cls) -> PetCareService:
        """Return the single shared PetCareService instance, creating it if needed."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # ------------------------------------------------------------------
    # Task management
    # ------------------------------------------------------------------

    def add_task(self, task: Task) -> None:
        """Add a task to the service's internal task list.

        Args:
            task: The Task to add.
        """
        # TODO: Append task to self._tasks
        self._tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from the service's internal task list.

        Args:
            task: The Task to remove.
        """
        # TODO: Remove task from self._tasks (handle case where task is not present)
        if task in self._tasks:
            self._tasks.remove(task)
        else:
            # Send a warning to the UI that the task was not found (optional)
            pass

    def update_task(self, task: Task) -> None:
        """Replace an existing task entry with updated values.

        Args:
            task: The Task with updated fields (matched by identity or title).
        """
        # TODO: Find the matching task in self._tasks and update its fields
        for i, existing_task in enumerate(self._tasks):
            if existing_task is task or existing_task.title == task.title:
                self._tasks[i] = task
                break
        else:
            # Send a warning to the UI that the task was not found (optional)
            pass
    
    def get_tasks_for_pet(self, pet: Pet) -> list[Task]:
        """Return a list of tasks associated with a given pet.

        Args:
            pet: The Pet whose tasks should be returned.

        Returns:
            A list of Task objects linked to the specified pet.
        """
        return [task for task in self._tasks if task.pet is pet]

    # ------------------------------------------------------------------
    # Scheduling
    # ------------------------------------------------------------------

    def generate_schedule(self) -> Schedule:
        """Build and return a Schedule from the current task list.

        Baseline algorithm:
        1. Sort tasks by time.
        2. Assign start times sequentially, halt the algorithm when there is a conflict.
        3. Populate Schedule.tasks and Schedule.description, then return it.

        Returns:
            A Schedule containing ordered tasks and a human-readable description.
        """
        # TODO: Sort self._tasks by time (tasks with time=None should be treated as unscheduled and sorted last)
        # TODO: Iterate over sorted tasks; use _is_conflict to detect overlaps
        # TODO: Assign task.time for non-conflicting tasks; halt on first conflict
        # TODO: Build schedule.description summarising the plan
        # TODO: Return the completed Schedule
        sortedTasksByTime = sorted(self._tasks, key=lambda t: (t.time is None, t.time))
        for i in range(len(sortedTasksByTime)):
            for j in range(i + 1, len(sortedTasksByTime)):
                if self._is_conflict(sortedTasksByTime[i], sortedTasksByTime[j]):
                    # we can alert the UI about the conflict by returning the tasks that are conflicting   
                    # and halt the algorithm when there is a conflict
                    break
        
        schedule = Schedule()
        schedule.tasks = sortedTasksByTime  # This is a placeholder; only non-conflicting tasks should be included
        schedule.description = "Generated schedule with {} tasks.".format(len(schedule.tasks))
        return schedule

    def _is_conflict(self, task1: Task, task2: Task) -> bool:
        """Check whether two tasks overlap in time.

        Args:
            task1: First task (must have task1.time set).
            task2: Second task (must have task2.time set).

        Returns:
            True if the tasks overlap; False otherwise.
        """
        # TODO: Compute end times for both tasks using time + timedelta(minutes=duration_minutes)
        # TODO: Return True if the intervals overlap, False if they are disjoint
        if task1.time is None or task2.time is None:
            return False  # Unschedulable tasks are not considered conflicting
        endTimeTask1 = task1.time + timedelta(minutes=task1.duration_minutes)
        endTimeTask2 = task2.time + timedelta(minutes=task2.duration_minutes)
        return endTimeTask2 >= task1.time and endTimeTask1 >= task2.time
