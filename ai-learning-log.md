## Fellow: <Uloko Emmanuella Emiene>
### Interaction #1 — <Test-first with unittest and assertRaises>
Problem: <I needed to learn how to test a function that should reject bad input, before writing change_status.>
My initial understanding: <I did not know how to start a test or why it must create a ticket first.>
Prompt to AI: <"i want to understand every concept and every bit of it" and "walk me through to solve it">
Useful AI guidance: <A test has three parts: set up, act, check. assertRaises(ValueError) passes only if the code raises that error. Write the test first and watch it fail.>
My independent experiment/test: <I wrote test_cannot_start_unassigned_ticket. With change_status containing only "pass", it failed with "AssertionError: ValueError not raised". After I wrote the real function, it passed.>
Verification source or result: <Output of python3 -m unittest test_workflow -v: FAIL first, then pass. Later, python3 -m unittest test_ticket test_workflow -v: Ran 22 tests, OK.>
Decision: <Accepted. The failure matched my prediction, so I trusted the test.>
Related file/commit: <test_workflow.py, workflow.py. SHA: 5d60727 >
What I can now explain without AI: <A test builds a ticket, calls the function and checks the result. A test that fails first proves it can really fail.>

### Interaction #2 — <Debugging imports and running tests>
Problem: <My test could not import change_status, and running the test file printed nothing.>
My initial understanding: <I thought python3 test_workflow.py would run my tests.>
Prompt to AI: <I pasted "ModuleNotFoundError: No module named 'workflow'" and the output of ls.>
Useful AI guidance: <Python cannot import file names with hyphens (work-flow.py). Running the file directly only defines the class, so use python3 -m unittest.>
My independent experiment/test: <I renamed the files with underscores and ran python3 -m unittest test_workflow -v.>
Verification source or result: <The ModuleNotFoundError disappeared and the test ran and showed FAIL, which was expected at that stage.>
Decision: <Accepted and applied.>
Related file/commit: <workflow.py, test_workflow.py. SHA: add yours>
What I can now explain without AI: <Import names cannot contain hyphens, and -m unittest starts the test runner.>

### Interaction #3 — <Validate before changing data, and checking AI advice>
Problem: <My first change_status draft was wrong, and I had to design the status rules.>
My initial understanding: <I put the status change inside the if that should reject the request, and my loop never saved the ticket in found.>
Prompt to AI: <"how to reject and change status">
Useful AI guidance: <Raise errors first and change the status only after every check passes. Store the allowed moves in a dictionary (ALLOWED).>
My independent experiment/test: <I fixed the order and wrote tests for skipping open -> resolved, the full path, reopening, resolved -> in_progress and an unknown ID.>
Verification source or result: <My tests check that a rejected change leaves the ticket's status unchanged, and all pass.>
Decision: <Improved and partly rejected. The AI suggested keeping "resolved" empty with a separate reopen function, but I chose "resolved": ["open"] and tested it. I also changed next_id to use the highest existing number instead of len(tickets) + 1, so IDs stay unique.>
Related file/commit: <workflow.py, ticket.py (next_id), test_workflow.py. SHA: add yours>
What I can now explain without AI: <Every check runs before the line that changes the status, because raise stops the function. ALLOWED[found["status"]] gives the statuses the ticket may move to.>