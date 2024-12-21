def format_name (first_name, last_name):
    formatted_first_name = first_name.title()
    formatted_second_name= last_name.title()
    return f"{formatted_first_name} {formatted_second_name}"

print(format_name("GabRRiel", "ToRres"))
