# Queue
consultation_queue = []
# ----------
def pet_id_generator(queue):
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
    while True:
        user_prompt = input(prompt)

        if user_prompt.strip() and all(x.isalpha() or x.isspace() for x in user_prompt):
            return user_prompt.title()
        else:
            field_name = prompt.strip().rstrip(":").strip().lower()
            print(f"Invalid input. '{user_prompt}' is not a valid {field_name}.")
# ----------
def get_severity_level():
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
# ----------
# Trial
register_pet(consultation_queue)
print(consultation_queue)
