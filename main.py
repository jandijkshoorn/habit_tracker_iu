import questionary
from db import get_db
from tracker import Tracker
from analyse import calculate_count, habits_list


def cli():
    db = get_db()
    questionary.confirm("Do you want to use preset habits?").ask()

    stop = False
    while not stop:
        main_menu = questionary.select(
            "Welcome to the main menu, what do you want to do?",
            choices=["Complete tasks", "Create new habit", "Analyse habits", "Delete habits", "Exit"]
        ).ask()

        if main_menu == "Complete tasks":
            name = questionary.text("What's the name of your counter?").ask()
            tracker = Tracker(name, "no description")
            tracker.increment()
            tracker.add_event(db)
        elif main_menu == "Create new habit":
            name = questionary.text("What's the name of your counter?").ask()
            desc = questionary.text("What is the description of your counter?").ask()
            tracker = Tracker(name, desc)
            tracker.store(db)
        elif main_menu == "Analyse habits":
            name = questionary.text("What's the name of your counter?").ask()
            choice = questionary.select(
                "Welcome to the main menu, what do you want to do?",
                choices=["List of all currently tracked habits", "List of all habits with the same periodicity", "Longest run streak of all defined habits", "Longest run streak for a given habit", "Back"]
            ).ask()
            if choice == "List of all currently tracked habits":
                count = calculate_count(db, name)
                print(f"{name} has been incremented {count} times")
            elif choice == "List of all habits with the same periodicity":
                print("Hello")
                stop = True
            elif choice == "Longest run streak of all defined habits":
                print("Bye!")
                stop = True
            elif choice == "Longest run streak for a given habit":
                print("Bye!")
                stop = True
            else:
                main_menu
        elif main_menu == "Delete habits":
            name = questionary.text("What's the name of your counter?").ask()
            print("You have chosen 'delete habits'!")
            return Tracker
        else:
            print("Bye!")
            stop = True


if __name__ == '__main__':
    cli()