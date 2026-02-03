import asyncio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

import PGConnect


LDTopKeys = ['ld top']
HDTopKeys = ['hd top']
LDBotKeys = ['ld bot', 'ld bottom']
LDRightKeys = ['ld right', 'right']
LDLeftKeys = ['ld left']
LDFiveKeys = ['ld five']
LDFullKeys = ['ld full']
HDFullKeys = ['hd full', 'hdf', '1']
HDBottomKeys = ['hd bottom']


def ask_for_geometry():
    while True:
        s = input("Enter module shape (e.g. ld top / hd full): ").strip().lower()

        if s in [x.lower() for x in LDTopKeys]: return 'LT'
        if s in [x.lower() for x in HDTopKeys]: return 'HT'
        if s in [x.lower() for x in LDBotKeys]: return 'LB'
        if s in [x.lower() for x in LDRightKeys]: return 'LR'
        if s in [x.lower() for x in LDLeftKeys]: return 'LL'
        if s in [x.lower() for x in LDFiveKeys]: return 'L5'
        if s in [x.lower() for x in LDFullKeys]: return 'LF'
        if s in [x.lower() for x in HDFullKeys]: return 'HF'
        if s in [x.lower() for x in HDBottomKeys]: return 'HB'

        print("Unrecognized shape. Try: ld top, hd full, ld bot, ...")


def ask_for_chip():
    while True:
        s = input("Enter chip (A/B/C/D or ALL or CD): ").strip().upper()
        if s in {"A", "B", "C", "D", "ALL", "", "2", "CD"}:
            return "ALL" if s in {"", "ALL"} else s
        print("Invalid chip. Use A/B/C/D/ALL/CD (or 2 if that's your B).")

async def main():
    # user input
    ShapeID = ask_for_geometry()
    Chip = ask_for_chip()

    rows = await PGConnect.read_db_pos()
    filtered = []
    for Module in rows:
        name = Module[0]

        # shape filter
        for Module in rows:
            if ShapeID in Module[0]:
                if Module[0][8].upper() == Chip or Chip == "ALL" or (Chip == "CD" and Module[0][8].upper() in ['C','D']):
                    filtered.append(Module)

    print(f"Total rows: {len(rows)} | Filtered rows: {len(filtered)}")
    if len(filtered) == 0:
        print("No modules matched your filters. Check ShapeID substring and chip position.")
        return None

    List_module_name = []
    List_rel_sensor_X = []
    List_rel_sensor_Y = []

    List_rel_pcb_X = []
    List_rel_pcb_Y = []

    for Module in filtered:
        List_module_name.append(Module[0])
        List_rel_sensor_X.append(Module[1] / 1000.0)
        List_rel_sensor_Y.append(Module[2] / 1000.0)
        List_rel_pcb_X.append(Module[4] / 1000.0)
        List_rel_pcb_Y.append(Module[5] / 1000.0)
        number = 100
        List_rel_sensor_X, List_rel_sensor_Y = List_rel_sensor_X[-number:], List_rel_sensor_Y[-number:]
        List_rel_pcb_X, List_rel_pcb_Y = List_rel_pcb_X[-number:], List_rel_pcb_Y[-number:]
        print(List_rel_sensor_X)

asyncio.run(main())