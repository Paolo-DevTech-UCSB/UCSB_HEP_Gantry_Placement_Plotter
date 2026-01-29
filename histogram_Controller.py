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


def plot_xy_with_marginals(
    x, y,
    bins=50,
    xlabel="x_offset (mm)",
    ylabel="y_offset (mm)",
    title=None
):
  
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)


    if x.size == 0 or y.size == 0:
        print("No data to plot (empty after filtering).")
        return

    fig = plt.figure(figsize=(7.5, 7.0))
    gs = GridSpec(4, 4, figure=fig)

    ax_scatter = fig.add_subplot(gs[1:4, 0:3])
    ax_histx = fig.add_subplot(gs[0, 0:3], sharex=ax_scatter)
    ax_histy = fig.add_subplot(gs[1:4, 3], sharey=ax_scatter)

    # Scatter
    ax_scatter.scatter(x, y, s=18, alpha=0.7)
    ax_scatter.set_xlabel(xlabel)
    ax_scatter.set_ylabel(ylabel)
    ax_scatter.grid(True, alpha=0.3)
    if title:
        ax_scatter.set_title(title)

    # X histogram
    ax_histx.hist(x, bins=bins)
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histx.set_ylabel("Counts")

    # Y histogram
    ax_histy.hist(y, bins=bins, orientation="horizontal")
    ax_histy.tick_params(axis="y", labelleft=False)
    ax_histy.set_xlabel("Counts")

    # Mean and stddev lines
    mu_x = np.mean(x)
    mu_y = np.mean(y)
    sx = np.std(x, ddof=1)
    sy = np.std(y, ddof=1)
    ax_scatter.scatter(mu_x, mu_y, color='red', marker='x', s=80)
    ax_histx.axvline(mu_x + sx, color='green', linestyle='--')
    ax_histx.axvline(mu_x - sx, color='green', linestyle='--')
    ax_histy.axhline(mu_y + sy, color='red', linestyle='--')
    ax_histy.axhline(mu_y - sy, color='red', linestyle='--')
    textstr = (
    f"$\\mu_x = {mu_x:.3f}$ mm\n"
    f"$\\sigma_x = {sx:.3f}$ mm\n"
    f"$\\mu_y = {mu_y:.3f}$ mm\n"
    f"$\\sigma_y = {sy:.3f}$ mm"
    )

    ax_scatter.text(
    0.65, 0.98,          
    textstr,
    transform=ax_scatter.transAxes,
    fontsize=11,
    verticalalignment='top',
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8)
    )

    plt.tight_layout()
    plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def plot_angle_r_with_marginals(
    angle, x, y,
    bins=50,
    xlabel="angle_offset (deg)",
    ylabel="r (mm)",
    title=None
):

    angle = np.asarray(angle, dtype=float)
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)


    # --- compute r ---
    r = np.sqrt(x**2 + y**2)

    fig = plt.figure(figsize=(7.5, 7.0))
    gs = GridSpec(4, 4, figure=fig)

    ax_scatter = fig.add_subplot(gs[1:4, 0:3])
    ax_histx   = fig.add_subplot(gs[0, 0:3], sharex=ax_scatter)
    ax_histy   = fig.add_subplot(gs[1:4, 3], sharey=ax_scatter)


    ax_scatter.scatter(angle, r, s=18, alpha=0.7)
    ax_scatter.set_xlabel(xlabel)
    ax_scatter.set_ylabel(ylabel)
    ax_scatter.grid(True, alpha=0.3)
    if title:
        ax_scatter.set_title(title)


    # angle histogram (top)
    ax_histx.hist(angle, bins=bins)
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histx.set_ylabel("angleoffset (deg)")

    # r histogram (right)
    ax_histy.hist(r, bins=bins, orientation="horizontal")
    ax_histy.tick_params(axis="y", labelleft=False)
    ax_histy.set_xlabel("r (mm)")

    mu_a = np.mean(angle)
    mu_r = np.mean(r)
    sa = np.std(angle, ddof=1)
    sr = np.std(r, ddof=1)

    ax_scatter.scatter(mu_a, mu_r, color='red', marker='x', s=80)

    ax_histx.axvline(mu_a + sa, color='green', linestyle='--')
    ax_histx.axvline(mu_a - sa, color='green', linestyle='--')
    ax_histy.axhline(mu_r + sr, color='red', linestyle='--')
    ax_histy.axhline(mu_r - sr, color='red', linestyle='--')

    textstr = (
        f"$\\mu_{{angle}} = {mu_a:.3f}$ deg\n"
        f"$\\sigma_{{angle}} = {sa:.3f}$ deg\n"
    )

    ax_scatter.text(
        0.65, 0.98,
        textstr,
        transform=ax_scatter.transAxes,
        fontsize=11,
        verticalalignment='top',
    )

    plt.tight_layout()
    plt.show()

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
    List_rel_sensor_angle = []
    List_rel_pcb_X = []
    List_rel_pcb_Y = []
    List_rel_pcb_angle = []
    for Module in filtered:
        List_module_name.append(Module[0])
        List_rel_sensor_X.append(Module[1] / 1000.0)
        List_rel_sensor_Y.append(Module[2] / 1000.0)
        List_rel_sensor_angle.append(Module[3])
        List_rel_pcb_X.append(Module[4] / 1000.0)
        List_rel_pcb_Y.append(Module[5] / 1000.0)
        List_rel_pcb_angle.append(Module[6])
        number = 1000
        List_rel_sensor_X, List_rel_sensor_Y = List_rel_sensor_X[-number:], List_rel_sensor_Y[-number:]
        List_rel_pcb_X, List_rel_pcb_Y = List_rel_pcb_X[-number:], List_rel_pcb_Y[-number:]
        List_rel_sensor_angle, List_rel_pcb_angle = List_rel_sensor_angle[-number:], List_rel_pcb_angle[-number:]


#    plot_xy_with_marginals(
#        List_rel_sensor_X,
#        List_rel_sensor_Y,
#        bins=50,
#        xlabel="Sensor x_offset (mm)",
#        ylabel="Sensor y_offset (mm)",
#        title=f"Shape={ShapeID}, Chip={Chip} (Sensor offsets)"
#    )

    # plot_xy_with_marginals(
    #     List_rel_pcb_X,
    #     List_rel_pcb_Y,
    #     bins=50,
    #     xlabel="PCB x_offset (mm)",
    #     ylabel="PCB y_offset (mm)",
    #     title=f"Shape={ShapeID}, Chip={Chip} (PCB offsets)"
    # )

    plot_angle_r_with_marginals(
    List_rel_sensor_X,
    List_rel_sensor_Y,
    List_rel_sensor_angle,
    title=f"Shape={ShapeID} , Chip={Chip} ,Sensor angle offset vs radial displacement",
)
    
#     plot_angle_vs_r_distribution(
#     List_rel_pcb_X, 
#     List_rel_pcb_Y,
#     List_rel_pcb_angle,
#     title=f"Shape={ShapeID} , Chip={Chip}, PCB angle offset vs radial displacement",
# )

if __name__ == "__main__":
    asyncio.run(main())
