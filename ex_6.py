from sys import argv

script, filename = argv

print(f"we'ra going to erase {filename}.")
print("if you don't want that, hit CTRL+C (^C).")
print("if you do want that, hit RETURN.")

input("?")
