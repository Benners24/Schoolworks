# Queue
consultation_queue = []

# ----------

def pet_id_generator(queue):
    """
    Generate a unique, sequential Patient ID (PID) for a new pet registration.

    Checks the provided queue to determine the next available ID. If the queue
    is empty, the ID starts at 'PID001'. Otherwise, it retrieves the last
    entry's ID, increments the numeric portion by 1, and returns the new ID
    zero-padded to 3 digits.

    Args:
        queue (list): The current consultation queue. Each element is expected
                      to be a dict whose sole key is a PID string
                      (e.g., {'PID003': { ... }}).

    Returns:
        str: A formatted patient ID string in the pattern 'PIDxxx',
             where 'xxx' is a zero-padded integer (e.g., 'PID001', 'PID012').
    """

    if queue == []:
        return 'PID001'
    else:
        last_info = queue[-1]
        last_pid = list(last_info.keys())[0]
        pid_prefix = last_pid[:3]
        pid_number = int(last_pid[3:]) + 1
        return f"{pid_prefix}{pid_number:03d}"
    
# ----------

def get_valid_input(prompt):
    """
    Prompt the user for a text input and validate that it contains only
    alphabetic characters and spaces (no numbers or special characters).

    Repeatedly prompts until a valid, non-empty input is provided.
    The accepted input is returned in title case (e.g., 'john doe' → 'John Doe').

    Args:
        prompt (str): The message displayed to the user when asking for input
                      (e.g., 'Pet Name: ', 'Owner Name: ').

    Returns:
        str: The validated user input converted to title case.

    Notes:
        - Inputs containing only spaces are considered invalid due to
          the `.strip()` check.
        - The field name shown in the error message is derived from the
          prompt itself by stripping whitespace and the trailing colon.
    """

    while True:
        user_prompt = input(prompt)

        if user_prompt.strip() and all(x.isalpha() or x.isspace() for x in user_prompt):
            return user_prompt.title()
        else:
            field_name = prompt.strip().rstrip(":").strip().lower()
            print(f"Invalid input. '{user_prompt}' is not a valid {field_name}.")

# ----------

def get_severity_level():
    """
    Prompt the user to select a condition severity level on a scale of 1 to 5
    and return a formatted string describing the selected level.

    Repeatedly prompts until a valid integer between 1 and 5 (inclusive) is
    entered. Non-numeric input is caught gracefully and the user is prompted
    again without crashing.

    Returns:
        str: A formatted string combining the numeric input and its label,
             in the form '<number> - <label>'
             (e.g., '1 - Most Severe / Emergency', '4 - Minor').

    Notes:
        - Non-numeric input is handled by a try/except ValueError block
          and will not raise an exception.
        - Severity options are stored in a dictionary (severity_map) for
          cleaner lookup and easier future maintenance.
    """

    severity_map = {
        1: "Most Severe / Emergency",
        2: "Serious",
        3: "Moderate",
        4: "Minor",
        5: "Least Severe"
    }

    while True:
        try:
            user_prompt = int(input("Condition Severity (1-5): "))
            if user_prompt in severity_map:
                return f"{user_prompt} - {severity_map[user_prompt]}"
            else:
                print(f"Invalid input. Severity level {user_prompt} is not valid.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

# ----------

def register_pet(queue):
    """
    Collect pet and owner details through user input, package them into a
    structured record, append it to the provided queue, and return the record.

    Calls the following helpers to build the registration form:
        - `pet_id_generator(queue)` → generates the unique patient ID (used as the key)
        - `get_valid_input()`       → collects and validates Pet Name, Breed, and Owner Name
        - `get_severity_level()`    → collects and validates the condition severity

    Args:
        queue (list): The consultation queue to append the new record to.
                      Passed explicitly to avoid reliance on a global variable.

    Returns:
        dict: The newly created registration record, with the generated PID
              as the key and the pet's details as the value.

    Notes:
        - The queue is mutated in place via `.append()`, so the caller's
          list is updated without needing to reassign it.
        - The PID is generated at the moment `form_data` is constructed,
          so it accurately reflects the queue's current length at the time
          of the call.
    """


    form_data = {
        pet_id_generator(queue): {
            "Pet Name"           : get_valid_input("Pet Name: "),
            "Breed"              : get_valid_input("Breed: "),
            "Owner Name"         : get_valid_input("Owner Name: "),
            "Condition Severity" : get_severity_level()
        }
    }

    queue.append(form_data)
    return form_data

while True:
    register_pet()
    print(consultation_queue)
        
