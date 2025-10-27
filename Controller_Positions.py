import asyncio
import numpy as np
import make_accuracy_plot_PositionsNColors, PGConnect

async def main():
    List = await PGConnect.read_db_pos()
    List_module_name = []
    List_rel_sensor_X = []
    List_rel_sensor_Y = []
    List_rel_sensor_angle = []
    List_rel_pcb_X = []
    List_rel_pcb_Y = []
    List_rel_pcb_angle = []
    List_Tray_Position = []
    number = 100

    for Module in List:
        if isinstance(Module[7], (list, tuple, np.ndarray)) and Module[7]:
            if np.average(Module[7]) > 200:
                List_Tray_Position.append(("P1",Module[8]))
            elif np.average(Module[7]) < 200:
                List_Tray_Position.append(("P2",Module[8]))
            List_module_name.append(Module[0])
            List_rel_sensor_X.append(Module[1]/1000)
            List_rel_sensor_Y.append(Module[2]/1000)
            List_rel_sensor_angle.append(Module[3])
            List_rel_pcb_X.append(Module[4]/1000)
            List_rel_pcb_Y.append(Module[5]/1000)
            List_rel_pcb_angle.append(Module[6])

        else:
            print(f"Skipping: {Module[0]}, No Y Points List")  # Debugging output




    #print(List_module_name)
    listA = [List_module_name[-number:], List_rel_sensor_X[-number:], List_rel_sensor_Y[-number:], List_rel_pcb_X[-number:],
              List_rel_pcb_Y[-number:], List_rel_sensor_angle[-number:], List_rel_pcb_angle[-number:],
                List_Tray_Position[-number:]]
    for Name in List_module_name[-number:]:
        print(Name)
        
    make_accuracy_plot_PositionsNColors.make_accuracy_plot(listA)

asyncio.run(main())
