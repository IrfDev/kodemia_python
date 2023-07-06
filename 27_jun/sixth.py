DEFAULT_NAMES = ['Juan','Pedro', 'Mauricio', 'David','Bossuet','Alexis']

computed_list_of_names = []

def run_first_script():
  import first_script as py1
  return py1.tupple_of_names
    
is_custom_name_list_input = input("Quieres escribir tu lista de nombres? y/n : ")

is_custom_name_list_boolean = is_custom_name_list_input.lower() == 'y'

if is_custom_name_list_boolean:
  computed_list_of_names = run_first_script()
else:
  computed_list_of_names = DEFAULT_NAMES.copy()

name_to_search = input("Ingresa un nombre para buscar en tu lista de nombres: ")

is_name_in_list = name_to_search in computed_list_of_names

if is_name_in_list:
  print(f"El nombre {name_to_search} se encuentra en la lista de nombres")
else:
  print(f"El nombre {name_to_search} NO se encuentra en la lista de nombres")