import json

def load_menu(path: str) -> dict:
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_menu(path: str, menu: dict) -> None:
    with open(path, 'w') as file:
        json.dump(menu, file, indent=4)

def add_menu_item(menu: dict, item: dict) -> dict:
    item_id = str(len(menu) + 1)
    menu[item_id] = item
    return menu

def update_menu_item(menu: dict, item_id: str, updates: dict) -> dict:
    if item_id in menu:
        for key, value in updates.items():
            menu[item_id][key] = value
    return menu

def filter_menu(menu: dict, category: str, vegetarian: bool | None = None) -> list:
    results = []
    for item_id, item in menu.items():
        if item['category'] == category:
            if vegetarian is None or item.get('vegetarian') == vegetarian:
                results.append(item)
    return results
