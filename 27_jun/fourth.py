import first_script as py1

def run_first_script():
  return py1.tupple_of_names
    
def calculate_repeated_names(original_name_list):
   new_list = []
   duplicated_list = []

   for name in original_name_list:
      if name not in new_list:
        new_list.append(name)
      else:
        duplicated_list.append(name)

   return set(duplicated_list)

list_of_names = run_first_script()

print(f"This was the result of the 1st script: {list_of_names}")

set_of_duplicated = calculate_repeated_names(list_of_names)

for name in set_of_duplicated:
  print(f"{name} found {list_of_names.count(name)} in list")