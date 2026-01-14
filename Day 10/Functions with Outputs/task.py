def format_name(first_name, last_name):
    name = first_name.title() + " " + last_name.title()
    return name

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

print(format_name(first_name=f_name, last_name=l_name))