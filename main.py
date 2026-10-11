from storage import list_and_view
from report import tickets_report
from workflow import changestatus
from ticket import main_main


def main():
    while True:
        print("Enter a key to select an option")
        print("F1 — CREATE: Collect ticket details, validate inputs, calculate priority, assign a unique ID and store the record")
        print("F2 — LIST / VIEW: Show all tickets and details for one chosen ticket.")
        print("F3 — ASSIGN: Assign a ticket to a non-empty staff member name; reject unknown ticket IDs.")
        print("F4 — WORKFLOW: Support open → in_progress → resolved. Do not move an unassigned ticket in)to in_progress. A resolved ticket may only be modified after an explicit reopen that sets it to open.")
        print("F5 — WORK QUEUE: Show open, unresolved tickets in critical → high → medium → low order; b)reak priority ties using the earlier numeric ticket ID.")
        print("F6 — REPORTS: Show total tickets and breakdowns by status and priority; handle zero ticke)ts correctly.")
        print("F7 — PERSISTENCE: Save to JSON and reload on startup. Missing file should allow a fresh s)tart; malformed JSON should produce a clear error rather tfhan silently erase data. IDs must remain unique after reload.")

        Userselct = input("Select an option here: ").upper()

        if Userselct == "F1":
            main_main()
        elif Userselct == "F2":
            list_and_view()
        elif Userselct == "F3":
            pass
        elif Userselct == "F4":
            changestatus()
        elif Userselct == "F5":
            pass
        elif Userselct == "F6":
            tickets_report()
        else:
            print("invalid option")
            return






