# Veterinary Clinic Management System

A simple Python-based **Veterinary Clinic Management System** that manages pet consultation queues using a **Priority Queue implemented with a Singly Linked List**.

This project allows veterinary staff to:

- Register pets
- Prioritize critical cases
- Serve pets in order of severity
- Undo registrations
- Display all registered pets
- View the current consultation queue

---

# Features

## Priority Queue System
Pets are automatically arranged based on their condition severity:

| Severity | Priority |
|----------|----------|
| 1 | Highest Priority |
| 5 | Lowest Priority |

- Lower severity number = higher priority
- Critical pets (`Severity 1`) are placed at the front of the queue

---

## Register Pet
Add a pet into the consultation queue with:

- Pet Name
- Breed
- Owner Name
- Condition Severity (1–5)

Each pet receives an auto-generated ID:

```text
PID001
PID002
PID003
```

---

## Serve Next Pet
Displays and removes the next pet from the queue.

Example:

```text
Now Serving:
Pet ID         : PID002
Pet Name       : Kirby
Breed          : Golden Retriever
Owner Name     : John
Severity Level : 2
```

---

## Undo Last Registration
Removes the most recently registered pet from:

- Queue
- Registry

---

## Display Registered Pets
Shows all pets currently stored in the registry.

---

## Queue Display
The system continuously displays:

- Current pet to be served
- Waiting line of pets

Example:

```text
CURRENT PET TO BE SERVED:
Pet ID         : PID002
Pet Name       : Kirby

WAITING LINE:
1. PID001 | Max | Doberman | Owner: John | Severity: 5
```

---

# Data Structures Used

## Singly Linked List

The consultation queue is implemented using:

- `Node` class
- `ConsultationQueue` class

Each node stores:

```python
data
next
```

---

## Priority Queue Logic

Queue ordering is based on:

1. Severity level
2. Pet ID order (FIFO for same severity)

---

# Program Structure

```text
Node Class
Pet Class
ConsultationQueue Class
Helper Functions
Core Functions
Menu System
```

---

# Functions Overview

| Function | Description |
|----------|-------------|
| `enqueue()` | Inserts pet according to priority |
| `dequeue()` | Serves the next pet |
| `register_pet()` | Registers a new pet |
| `undo_register()` | Removes last registration |
| `display_registry()` | Displays all registered pets |
| `display_queue()` | Displays current queue |
| `menu()` | Main menu loop |

---

# Input Validation

The system validates:

- Empty inputs
- Invalid characters
- Severity range (1–5)

Example:

```text
Invalid input. Please enter a number between 1 and 5.
```

---

# How to Run

## Requirements

- Python 3.x

## Run the program

```bash
python filename.py
```

---

# Sample Menu

```text
MENU
[1] Register Pet
[2] Serve Next Pet
[3] Undo Last Registration
[4] Display Registered Pets
[5] Exit
```

---

# Sample Critical Warning

```text
WARNING: Pet PID003 is in critical condition!
Severity: 1 — placing at highest priority.
```

---

# Concepts Demonstrated

This project demonstrates:

- Object-Oriented Programming (OOP)
- Singly Linked Lists
- Priority Queues
- Queue Management Systems
- Input Validation
- Menu-Driven Console Applications

---

# Authors

Developed by:

- Adalim, Isaiah
- Legaspi, John Benedict
- Marcelo, Chloe
- Mercado, Brian
- Mirador, Josh Matthew

Developed as a Python Data Structures and Algorithms project.
