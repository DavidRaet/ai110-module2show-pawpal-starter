# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

A user should be able to do... 

1. Provide their own basic information and their pet 
2. CRUD a pet care task (Create, Read, Update, Delete)
3. The assistant should also accommodate specific features such as 
time availability and priority of a task, and the owner's preferences.   
4. Generate a schedule based on those tasks and a description that explains
the given schedule.  

Classes that should be defined including its individual attributes and methods:

class Preferences
  - reminderTime: String

class Owner
  - name: String
  - preferences: Preferences
  - pets: Pet[]

class Pet
  - name: String
  - age: int
  - breed: String
  - species: enum Species {Cat, Dog, Other}

class Task
  - title: String
  - durationMinutes: int
  - time: DateTime
  - priority: enum Priority {High, Medium, Low}
  - status: enum Status {Pending, Completed, Skipped}
  - pet: Pet

class Schedule
  - tasks: Task[]
  - description: String

class PetCareService (singleton)
  - addTask(Task): void
  - removeTask(Task): void
  - updateTask(Task): void
  - generateSchedule(Schedule): Schedule
  - isConflict(Task, Task): boolean
    └─ (used internally by generateSchedule)

Connections:
Owner has multiple Pets (Owner -1*> Pet)

Pets --> Tasks (Pets can have multiple Tasks)
Tasks can be tied to one Pet (Tasks -1> Pet)
Schedule can have multiple Pets (Schedule -1*> Pet)
Schedule can have one Owner (Schedule -> Owner)

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
