from storage import list_and_view
from report import tickets_report
from workflow import change_status
from ticket import main_main


def main():
    while True:
        print("\nSelect an option:")
        print("F1 - CREATE: Create a new ticket")
        print("F2 - LIST / VIEW: View tickets")
        print("F3 - ASSIGN: Assign a ticket")
        print("F4 - WORKFLOW: Change ticket status")
        print("F5 - WORK QUEUE: View unresolved tickets")
        print("F6 - REPORTS: View ticket reports")
        print("F7 - PERSISTENCE: Save and load tickets")
        print("Q - QUIT")

        user_select = input("Select an option: ").strip().upper()

        if user_select == "F1":
            main_main()
        elif user_select == "F2":
            list_and_view()
        elif user_select == "F3":
            print("Assignment feature is not implemented yet.")
        elif user_select == "F4":
            change_status()
        elif user_select == "F5":
            print("Work queue feature is not implemented yet.")
        elif user_select == "F6":
            tickets_report()
        elif user_select == "F7":
            print("Persistence feature is not implemented yet.")
        elif user_select == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()