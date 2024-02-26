# CRUDS operations for an item domain.
import time
field_names = ["Item Id", "Description", "Price"]
items = []
file_name = "items.dat"

def load_items():
	global items
	try:
		data_file = open(file_name, "r")
		data = data_file.read()
		# print(repr(data))
		if data:
		    items = eval(data)
		else:
		    items = []
		data_file.close()
	except FileNotFoundError:
		items = []
			

def show_items():
	for item in items:
		for value in range(len(item)):
			print(f"{field_names[value]}: {item[value]}")
		print("\n")

def show_success_message(item_id, operation):
	if(operation == "Update"):
		print(f"Item with Id {item_id} price has been updated.")
	else:
		print(f"Item with Id {item_id} has been deleted.")

def show_item_not_found_message(item_id):
	print(f"Item with Id {item_id} is not found.")

def update_delete_or_search_item(item_id, operation):
	item_found = False
	for item in items:
		if(item[0] == item_id):
			item_found = True
			if(operation == "Update"):
				newPrice = input("Enter new price: ")
				item[2] = newPrice
				show_success_message(item_id, operation)
				break
			elif(operation == "Delete"):
				items.remove(item)
				show_success_message(item_id, operation)
				break
			else:
				print("\n")
				for value in range(len(item)):
					print(f"{field_names[value]}: {item[value]}")
				print("\n")
				break

	save_items()	
	if(item_found == False):
		show_item_not_found_message(item_id)

def get_item_id():
	item_id = input("Enter item id: ")
	return item_id

def update_item():
	update_delete_or_search_item(get_item_id(), "Update")
	
def delete_item():
	update_delete_or_search_item(get_item_id(), "Delete")

def search_item():
	update_delete_or_search_item(get_item_id(), "Search")

def generate_data():
	
	for count in range(50000):
		item = []
		item_id = f"00{count + 1}"
		item.append(item_id)
		description = f"A{count}"
		item.append(description)
		price = f"{100 + count}"
		item.append(price)
		items.append(item)
	# return item	

# def get_item_details():
# 	item = []
# 	for field in field_names:
# 		item.append(input(f"Enter {field}: "))
# 	return item

def save_items():
	data_file = open(file_name, "w")
	data_file.write(str(items))
	data_file.close()

def create_item():
	# item = get_item_details()
	generate_data()
	# items.append(item)
	# print(items)
	save_items()

def get_user_choice():
	choice = int(input("\nPlease select an option: "))
	return choice

functions = [create_item, show_items, update_item, delete_item, search_item]

def show_menu():

	while True:
		print("1. Add Item")
		print("2. Show All Items")
		print("3. Update Item Price")
		print("4. Delete Item")
		print("5. Search Item")
		print("Enter 0 to Exit")
		choice = get_user_choice()
		if choice == 0:
			exit()
		elif (choice > 5 or choice < 0):
			print("Invalid option. Please select an appropriate option. ")
		
		if(choice > 0 and choice <= 5):
			start = time.time()
			start_time = time.process_time()
			functions[choice - 1]()
			end_time = time.process_time()
			end = time.time()
			cpu_time = end_time - start_time
			elapsed_time = end - start
			print(f"CPU time: {cpu_time} seconds")
			print(f"Elapsed Time: {elapsed_time} seconds")

start = time.time()		
start_time = time.process_time()
load_items()
end_time = time.process_time()
end = time.time()
cpu_time = end_time - start_time
elapsed_time = end - start
print(f"CPU time to load the records: {cpu_time} seconds")
print(f"Elapsed time to load records: {elapsed_time} seconds")
show_menu()
