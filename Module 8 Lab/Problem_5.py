# Joseph
# 11/30/2023

# Checks whether the game character has picked up all the items need to perform certain tasks
if check_tasks(character_items, character_debuffs):
    tasks = {
        "Climb a mountain": {"requires_items": ["rope" , "coat", "first aid kit"], "forbidden_debuff": "slow"},
        "Cook a meal": {"required_items": ["pan","groceries"], "forbidden_debuff": "small"},
        "Write a book": {"required_items": ["pen" , "paper","idea"], "forbidden_debuff": "confusion"}
    }

    for task, details in task.items():
        required_items = details["required_items"]
        forbidden_debuff = details["forbidden_debuff"]

        items_present = all(item in character_items for item in required_items)

        debuff_present = forbidden_debuff in character_debuffs

        if items_present and not debuff_present:
            print(f"Task '{task}' can be performed.")
        else:
            print(f"Task '{task}' cannot be performed.")