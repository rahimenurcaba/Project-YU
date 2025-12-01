import json
import os
import shutil
import datetime

def load_state(data_dir: str) -> tuple[list, dict, list]:
    tables = []
    menu = {}
    orders = []

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    try:
        with open(f"{data_dir}/tables.json", 'r') as f:
            tables = json.load(f)
    except:
        pass

    try:
        with open(f"{data_dir}/menu.json", 'r') as f:
            menu = json.load(f)
    except:
        pass

    try:
        with open(f"{data_dir}/orders.json", 'r') as f:
            orders = json.load(f)
    except:
        pass

    return tables, menu, orders

def save_state(data_dir: str, tables: list, menu: dict, orders: list) -> None:
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    with open(f"{data_dir}/tables.json", 'w') as f:
        json.dump(tables, f, indent=4)
    
    with open(f"{data_dir}/menu.json", 'w') as f:
        json.dump(menu, f, indent=4)
        
    with open(f"{data_dir}/orders.json", 'w') as f:
        json.dump(orders, f, indent=4)

def backup_day(data_dir: str, archive_dir: str) -> str:
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
        
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{archive_dir}/backup_{timestamp}"
    shutil.copytree(data_dir, backup_path)
    return backup_path

def log_kitchen_ticket(order: dict, directory: str) -> str:
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    filename = f"{directory}/ticket_{order['table_number']}.txt"
    with open(filename, 'w') as f:
        f.write(f"Table: {order['table_number']}\n")
        for item in order['items']:
            f.write(f"- {item['quantity']}x {item['name']} ({item.get('note', '')})\n")
            
    return filename
