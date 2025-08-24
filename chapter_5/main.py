import accesory_file

variable1 = "Python"
variable2 = "Zen"

control_var = 1
print(globals()[f"variable{control_var}"])

control_var = 2
print(globals()[f"variable{control_var}"])

control_var = 3
print(getattr(accesory_file, f"variable{control_var}"))

control_var = 4
print(getattr(accesory_file, f"variable{control_var}"))
