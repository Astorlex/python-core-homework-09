contacts = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command. Please try again"
    return wrapper


@input_error
def add_contact(command):
    parts = command.split(' ', 2)
    name, phone = parts[1], parts[2]

    if name in contacts.keys():
        return f'Contact with name {name} already exists'
    
    elif phone in contacts.values():
        return f'Contact with phone {phone} already exists'

    contacts[name] = phone
    return f"Added {name} with phone number {phone}"


@input_error
def change_contact(command):
    parts = command.split(' ', 2)
    name, phone = parts[1], parts[2]

    if name not in contacts.keys():
        return f'Contact with name {name} does not exist'
    
    elif phone in contacts.values():
        return f'Contact with phone {phone} already exists'
    
    else:
        contacts[name] = phone
        return f"Changed phone number for {name} to {phone}"


@input_error
def get_phone(command):
    name = command.split(' ', 1)[1]
    return contacts.get(name, f"No phone number found for {name}")


@input_error
def show_all():
    if contacts:
        return [f"{name:20} {phone}" for name, phone in contacts.items()]
    else:
        return None


def bye():
    print("Good bye!")


def main():
    print("Welcome! How can I help you?")
    while True:
        user_input = input("> ")
        user_input_lower = user_input.lower()

        if user_input == "hello":
            print("How can I help you?")
        elif user_input_lower.split(' ')[0] == "add":
            print(add_contact(user_input))
        elif user_input_lower.split(' ')[0] == "change":
            print(change_contact(user_input))
        elif user_input_lower.split(' ')[0] == "phone":
            print(get_phone(user_input))
        elif user_input_lower == "show all":
            all_contacts = show_all()

            if not all_contacts:
                print('You have no contacts')
            else:
                all_contacts.sort()
                print('\n'.join(all_contacts))

        elif user_input_lower in ["good bye", "close", "exit"]:
            bye()
            break
        elif not user_input_lower:
            continue
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit, EOFError):
        print('\n')
        bye()
