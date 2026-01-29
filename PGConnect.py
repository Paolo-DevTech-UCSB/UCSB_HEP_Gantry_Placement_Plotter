
import asyncpg
import asyncio
import json
import os

async def read_db():
    # Load config from desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "DBconfig.json")
    with open(desktop_path, "r") as f:
        config = json.load(f)

    # Connect using loaded config
    conn = await asyncpg.connect(**config)

    # Query the table
    mod_rows = await conn.fetch('SELECT module_name, x_offset_mu, y_offset_mu, ang_offset_deg FROM module_inspect')
    pm_rows = await conn.fetch('SELECT proto_name, x_offset_mu, y_offset_mu, ang_offset_deg FROM proto_inspect')

    Module_List = []; Proto_List = []; CompiledList = []
    for row in mod_rows:
        for rog in pm_rows:
            #print( row['module_name'][-8:], "vs",  rog['proto_name'][-8:])
            if row['module_name'][-10:] == rog['proto_name'][-10:]:
                if not any(sub in row['module_name'][-10:] for sub in ['dum', 'run', 'dry', 'Dry', 'Run']): 
                    #print( row['module_name'][-10:], "vs",  rog['proto_name'][-10:])
                    CompiledList.append((
                        row['module_name'],
                        row['x_offset_mu'],
                        row['y_offset_mu'],
                        row['ang_offset_deg'],
                        rog['x_offset_mu'],
                        rog['y_offset_mu'],
                        rog['ang_offset_deg']
                    ))



    #for module in CompiledList:
        #print(module)

    await conn.close()

    return CompiledList




async def read_db_pos():
    # Load config from desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "DBconfig.json")
    with open(desktop_path, "r") as f:
        config = json.load(f)

    # Connect using loaded config
    conn = await asyncpg.connect(**config)

    mod_rows = await conn.fetch('SELECT module_name, x_offset_mu, y_offset_mu, ang_offset_deg, y_points FROM module_inspect')
    pm_rows = await conn.fetch('SELECT proto_name, x_offset_mu, y_offset_mu, ang_offset_deg FROM proto_inspect')
    tray_rows = await conn.fetch('SELECT module_name, ass_tray_id FROM module_assembly')

    # Create lookup dictionaries for fast access
    proto_lookup = {
        rog['proto_name'][-10:]: (
            rog['x_offset_mu'],
            rog['y_offset_mu'],
            rog['ang_offset_deg']
        )
        for rog in pm_rows
    }

    tray_lookup = {
        tray['module_name']: tray['ass_tray_id']
        for tray in tray_rows
    }

    CompiledList = []

    for row in mod_rows:
        mod_key = row['module_name'][-10:]
        if mod_key in proto_lookup:
            if not any(sub in mod_key for sub in ['dum', 'run', 'dry', 'Dry', 'Run']):
                proto_data = proto_lookup[mod_key]
                tray_id = tray_lookup.get(row['module_name'], None)
                CompiledList.append((
                    row['module_name'],
                    row['x_offset_mu'],
                    row['y_offset_mu'],
                    row['ang_offset_deg'],
                    proto_data[0],  # proto x_offset_mu
                    proto_data[1],  # proto y_offset_mu
                    proto_data[2],  # proto ang_offset_deg
                    row['y_points'],
                    tray_id          # tray ID
                ))
    #for module in CompiledList:
        #print(module)

    await conn.close()

    return CompiledList