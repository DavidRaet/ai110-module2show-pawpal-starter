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

So, when ideating on the class of schedule, I changed the location of it's "generate_schedule" method
to a PetCareService class that is responsible for handling all of the business logic such as CRUD'ing 
tasks. I figured that I would separate the role of schedule as the entity that stores the sorted list of 
tasks, and the implementation of its creation as part of the PetCareService. Overall, I made this change
to accommodate separation of concerns of the schedule class and the method that creates it. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The main constraints I considered when planning the scheduler was priority and time. 
What mattered for me when I decided the constraint was simplicity. I believed that
priority was much easier to manage than time because you only had to sort tasks based 
on a small set of priority values. Compared to time, there was more to think about such as
formatting, checking for conflict, etc. 

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
So, for this scheduler, I believe that granularity was sacrificed for simplicity. 
There may be cases that the user wanted to label a specific time to start a task plus 
the priority. However, since I was aiming for simplicity, I chose to go with an algorithm
that sorts based on priority. 
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

Throughout the project I constantly ran through a lot of brainstorming and implementation rounds. 
For example, I would often make the first draft of a diagram and ask the AI to provide feedback and
suggestions that may develop the diagram further. 

So, I found that prompts that always stated the context of my plan, caveats it should follow, 
and a balance of specificity and conciseness gave me the most valuable outputs. I believe having the 
AI always asking you clarifying questions and giving its assumptions allows you to bring the most 
potential out of the LLM because it requires you to be very minute and mindful with your prompts. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

When I was focusing on integrating the UI to the backend, I prompted the AI to refactor 
the UI so that it was a skeleton that would accommodate the features of my backend. 
However, the moment I spotted that it wrote code that was similar to the backend, I halted to 
accept the output and clarified that the refactored UI the AI was outputting was all placeholder
and that once the skeleton was created, we would shift to refactor the UI again to integrate the 
pawpal_system. 

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

For the test suite, I wrote tests that primarily verified the expected behavior of the 
PetCareService. These tests were key to catching unexpected bugs, serving as self-documentation that confirms the intent of my intial designs, and forces me to battle-test my own architecture. 

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I have good confidence that my scheduler works as intended as I've only made it so
it sorts based on priority and the duration of the tasks in ascending order. If I wanted 
to test more edge cases, I'd want to test two tasks that have both the same duration and priority. 

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I was satisfied with being able to articulate my designs into diagrams and leveraging AI as both a 
sparring partner and informant. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would then find a way to change the scheduler algorithm so that it can accommodate both
priority and time. 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

I believe the most important thing I learned about designing systems and collaborating with AI
is being able to turn a vague design into something specific and detailed. Then, having AI 
further develop my ideas through the socratic method and serve as a secondary tutor. 