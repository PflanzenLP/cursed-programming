def do_step() -> None: ...
def place() -> None: ...
def turn_left() -> None: ...

# instead of:
for _ in range(5):
    do_step()
    place()
    for _ in range(2):
        turn_left()
    do_step()

# i did:
for _ in range(5):
    do_step()
    place()
    turn_left()
    turn_left()
    do_step()