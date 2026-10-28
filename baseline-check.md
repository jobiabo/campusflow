Initial audit observations
JSON storage: Ticket data is stored in tickets.json. Loading and saving logic is spread across more than one file (the load/save code in ticket.py and storage.py). Tickets are not validated when they are loaded, so a ticket with a missing or wrong field would be accepted.
Broken JSON: A malformed tickets.json has not been tested. The program may crash with a traceback instead of a clear message, and saving after a failed load could overwrite real data with an empty list.
Menu (F7): The F7 menu option prints "Persistence feature is not implemented yet", although saving and loading already work in the background after create, assign and status changes.
Ticket notes: The current ticket structure does not include a notes field.
Search: A ticket search feature with combined filters has not yet been implemented.
Reports: The existing report logic labels a status as "Closed", but the workflow uses resolved. The labels and the status strings need to match open, in_progress and resolved.
ID handling: Ticket IDs are generated from the highest existing numeric ticket ID, so IDs stay unique after a reload and after gaps. Note ID generation and validation still need to be implemented.
Input validation: Affected users typed as text or a decimal (such as abc or 2.5) used to show Python's own error message. This now shows a clear message. The category prompt now lists Other.
Test discovery: test_assign-queue.py had a hyphen in its filename, so Python's standard unittest discovery could not import it. It has been renamed to test_assign_queue.py. The full suite runs 32 tests, and the 22 tests in test_ticket.py and test_workflow.py pass on their own.
Repository hygiene: __pycache__/ and tickets.json were tracked by Git. They were removed from tracking and are now listed in .gitignore.
Integration: main.py imports storage, which does not exist on this branch, so the menu cannot start until the storage and report modules are merged