def check_item_exist(check_item, all_items):
    all_items = set(all_items)
    if check_item in all_items:
        return True
    else:
        return False


items = input().split(", ")

command = input()

while not command == "Craft!":
    type_command = command.split(" - ")[0]
    item = command.split(" - ")[1]
    is_exist = check_item_exist(item, items)
    if type_command == "Collect" and not is_exist:
        items.append(item)
    elif type_command == "Drop" and is_exist:
        items.remove(item)
    elif type_command == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        is_exist = check_item_exist(old_item, items)
        if is_exist:
            index = items.index(old_item)
            items.insert(index + 1, new_item)
    elif type_command == "Renew" and is_exist:
        index = items.index(item)
        x = items.pop(index)
        items.append(x)
    command = input()

print(", ".join(items))