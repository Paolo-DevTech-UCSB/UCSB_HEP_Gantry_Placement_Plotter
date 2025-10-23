####################################################################################
#
#  Filename    : EvtGenNtuplizer.cc
#  Description : Make an accuracy plot with offsets and angles of HGCAL 
#                module components w.r.t. baseplate components
#  Author      : You-Ying Li [ you-ying.li@cern.ch ]
#
####################################################################################

#################################
# Modified by Paolo Jordano     
# pjordano@ucsb.edu             
# Mod Version 0.2
#################################

# 0.1: Simplified for Use in Jupyter Notebook
# 0.2: Added an orientation setting

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
import matplotlib as mpl
mpl.use('Agg')

def make_accuracy_plot(List):
    
    List_module_name = List[0];
    List_rel_sensor_X = List[1];
    List_rel_sensor_Y = List[2];
    List_rel_pcb_X = List[3];
    List_rel_pcb_Y = List[4];
    List_rel_sensor_angle = List[5];
    List_rel_pcb_angle = List[6];
    
    module_name = 'LDMX Modules'
        
        ############################ || ORIENTATION SETTINGS || #######################
    """
    

    turncw = 0; ##<<<------ change turn settings here
    
    placeholder = 0;
    if turncw == -90 or turncw == 270:
        placeholder = rel_sensor_X;
        rel_sensor_X = -1*rel_sensor_Y;
        rel_sensor_Y = placeholder;
        
        placeholder = rel_pcb_X;
        rel_pcb_X = -1*rel_pcb_Y;
        rel_pcb_Y = placeholder
        print("270 clockwise turn confirmed");
        print("check that channel 1 started in the Top Right.")
    elif turncw == -180 or turncw == 180:
        rel_sensor_X = rel_sensor_X*-1;
        rel_sensor_Y = rel_sensor_Y*-1;
        
        rel_pcb_X = rel_pcb_X*-1
        rel_pcb_Y = rel_pcb_Y*-1
        print("180 clockwise turn confirmed");
        print("check that channel 1 started in the Bottom Right.")
    elif turncw == -270 or turncw == 90:
        placeholder = rel_sensor_X;
        rel_sensor_X = rel_sensor_Y;
        rel_sensor_Y = -1*placeholder;
        
        placeholder = rel_pcb_X;
        rel_pcb_X = rel_pcb_Y;
        rel_pcb_Y = -1*placeholder;
        print("90 clockwise turn confirmed ")
        print("check that channel 1 started in the Bottom left.")
    else:
        print("This code assumes channel 1 is in the Top Left.");
        print("Change settings if this is not the case.");
        print("No Rotation Used.")
    """
######################################################################

    """
    rel_sensor_X : relative X of sensor w.r.t. baseplate [unit : mm]
    rel_sensor_Y : relative Y of sensor w.r.t. baseplate [unit : mm]
    rel_pcb_X    : relative X of pcb w.r.t. baseplate    [unit : mm]
    rel_pcb_Y    : relative Y of pcb w.r.t. baseplate    [unit : mm]
    rel_sensor_angle : relative angle of sensor w.r.t. baseplate [unit : degree]
    rel_pcb_angle    : relative angle of pcb w.r.t. baseplate    [unit : degree]
    """

    
#  if len(data_list) == 1:
#       module_name = data_list[0].split()[0]
#   elif len(data_list) > 1:
#       module_name = "Merged"

    fig, ax = plt.subplots(figsize=(6,6), layout='constrained')
    ax.set_box_aspect(1)
    ax.set_title(f'{module_name} accuracy plot', y=1.15, fontsize=20)


    #################################
    #          Offset part          #
    #################################

    ax.set_xlabel('$\Delta x$ [$\mu m$]',  fontsize=18)
    ax.set_ylabel('$\Delta y$ [$\mu m$]', fontsize=18)
    ax.xaxis.set_major_locator(MultipleLocator(100))
    ax.yaxis.set_major_locator(MultipleLocator(100))
    ax.xaxis.set_minor_locator(MultipleLocator(25))
    ax.yaxis.set_minor_locator(MultipleLocator(25))
    ax.set_xlim(-200, 300)
    ax.set_ylim(-200, 300)
    ax.vlines(-50, -50, 50, colors='b')
    ax.vlines( 50, -50, 50, colors='b')
    ax.hlines(-50, -50, 50, colors='b')
    ax.hlines( 50, -50, 50, colors='b')
    ax.text(-50, 55, '50 $\mu m$', color='b', fontsize=12)
    ax.vlines(-100, -100, 100, colors='r')
    ax.vlines( 100, -100, 100, colors='r')
    ax.hlines(-100, -100, 100, colors='r')
    ax.hlines( 100, -100, 100, colors='r')
    ax.text(-100, 105,'100 $\mu m$', color='r', fontsize=12)
#    ax.vlines(0, -200, 300, colors='k')
#    ax.hlines(0, -200, 300, colors='k')

    for i in range(len(List_module_name)):
        
        rel_sensor_X = List_rel_sensor_X[i] * 1000  #Modified here to have Manual Input
        rel_sensor_Y = List_rel_sensor_Y[i] * 1000
        rel_pcb_X    = List_rel_pcb_X[i] * 1000
        rel_pcb_Y    = List_rel_pcb_Y[i] * 1000
        
        rel_sensor_X = List_rel_sensor_X[i] * 1000  #Modified here to have Manual Input
        rel_sensor_Y = List_rel_sensor_Y[i] * 1000
        rel_pcb_X    = List_rel_pcb_X[i] * 1000
        rel_pcb_Y    = List_rel_pcb_Y[i] * 1000
        
        limit_func = lambda x: 115. if x > 100. else -115. if x < -100. else x
        
        m_rel_sensor_X = limit_func( rel_sensor_X )  
        m_rel_sensor_Y = limit_func( rel_sensor_Y )
        m_rel_pcb_X    = limit_func( rel_pcb_X    )
        m_rel_pcb_Y    = limit_func( rel_pcb_Y    )
        
        
        ax.plot(m_rel_sensor_X, m_rel_sensor_Y, marker='o', markerfacecolor='#ff7f0e', markeredgecolor='#ff7f0e', linestyle = 'None', label = 'Sensor w.r.t. Baseplate')
        ax.plot(m_rel_pcb_X,    m_rel_pcb_Y,    marker='o', markerfacecolor='#2ca02c', markeredgecolor='#2ca02c', linestyle = 'None', label = 'PCB w.r.t. Baseplate')
        
        #if abs(m_rel_sensor_X) > 100. or abs(m_rel_sensor_Y) > 100.:
        #    ax.text(m_rel_sensor_X, m_rel_sensor_Y, f'({rel_sensor_X:.0f}, {rel_sensor_Y:.0f})', color='#ff7f0e',
        #            ha='right' if m_rel_sensor_X < -100. else 'left', va='top' if m_rel_sensor_Y < -100. else 'bottom')
        #
        #if abs(m_rel_pcb_X) > 100. or abs(m_rel_pcb_Y) > 100.:
        #    ax.text(m_rel_pcb_X, m_rel_pcb_Y, f'({rel_pcb_X:.0f}, {rel_pcb_Y:.0f})', color='#2ca02c',
        #            ha='right' if m_rel_sensor_X < -100. else 'left', va='top' if m_rel_sensor_Y < -100. else 'bottom')
        
        
        
        ax.plot(np.array([0.]), np.array([0.]), marker='o', markerfacecolor='k', markeredgecolor='k', linestyle = 'None', label = 'Baseplate')
        
        
        plt.tick_params(axis='both', which='minor', direction='in', labelsize=0, length=5, width=1, right=True, top=True)
        plt.tick_params(axis='both', which='major', direction='in', labelsize=18, length=7, width=1.5, right=True, top=True)
        
        
        # Legend is hardcore 
        legend_elements = [ Line2D([0], [0], marker='o', color='w', label='Sensor w.r.t. Baseplate', markerfacecolor='#ff7f0e'),
                            Line2D([0], [0], marker='o', color='w', label='PCB w.r.t. Baseplate',    markerfacecolor='#2ca02c'),
                            Line2D([0], [0], marker='o', color='w', label='Baseplate',               markerfacecolor='k')
                            ]
        
        ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower right', ncol=2, borderaxespad=0., handles=legend_elements)
        
        
    # Outside boundary region  ITS RIGHT HERE 
    ax.fill_between([-125, 125], 100, 125, color='r', alpha=0.05, linewidth=0)
    ax.fill_between([-125, 125], -100, -125, color='r', alpha=0.05, linewidth=0)
    ax.fill_between([-125, -100], -100, 100, color='r', alpha=0.05, linewidth=0)
    ax.fill_between([125, 100], -100, 100, color='r', alpha=0.05, linewidth=0)
    #    ax_sub.fill_between(-1. * node, 0, 2, color='r', alpha=0.1)
        
        
        
    #################################
    #      Rotation angle part      #
    #################################
    #ax_sub = fig.add_axes([.52, .58, .42, .25], polar=True)
    ax_sub = fig.add_axes([.50, .59, .42, .25], polar=True)
    
    gauge_angle_max  = 0.04
    gauge_angle_unit = 0.02
    orig_gauge_angle_max  = 40.
    transfer_factor = orig_gauge_angle_max / gauge_angle_max
    #transfer_factor = 40. / gauge_angle_max
    orig_gauge_angle_unit = transfer_factor * gauge_angle_unit
    
    ax_sub.set_rmax(2)
    ax_sub.get_yaxis().set_visible(False)
    ax_sub.grid(False)
    
    ax_sub.set_theta_offset(np.pi/2)
    ax_sub.set_thetamin(-orig_gauge_angle_max*1.2)
    ax_sub.set_thetamax(orig_gauge_angle_max*1.2)
    ax_sub.set_rorigin(-2.5)
    
    
    #tick = [ax_sub.get_rmax(),ax_sub.get_rmax()*0.97]
    #for t  in np.deg2rad(np.arange(0,360,orig_gauge_angle_unit*0.5)):
    #    ax_sub.plot([t,t], tick, lw=0.72, color="k")
    
    #tick = [ax_sub.get_rmax(),ax_sub.get_rmax()*0.9]
    #for t  in np.deg2rad(np.arange(0,360,orig_gauge_angle_unit)):
    #    ax_sub.plot([t,t], tick, lw=0.72, color="k")
    
    
    degree = ['{}°'.format(deg) for deg in np.round(np.arange(gauge_angle_max, -gauge_angle_max-gauge_angle_unit, -gauge_angle_unit), decimals=2)]
    
    ax_sub.set_thetagrids( np.arange(orig_gauge_angle_max, -orig_gauge_angle_max-orig_gauge_angle_unit, -orig_gauge_angle_unit) )
    ax_sub.set_xticklabels( degree )
    
    
    
    for i in range(len(List_module_name)):
                       
        rel_sensor_angle = List_rel_sensor_angle[i]  #Modified here to have Manual Input
        rel_pcb_angle    = List_rel_pcb_angle[i]
    
        limit_angle_func = lambda x: orig_gauge_angle_max * 1.1 if x > orig_gauge_angle_max else -orig_gauge_angle_max * 1.1 if x < -orig_gauge_angle_max else x
        orig_rel_sensor_angle = limit_angle_func(transfer_factor * rel_sensor_angle)
        orig_rel_pcb_angle    = limit_angle_func(transfer_factor * rel_pcb_angle)
        
        #if abs(orig_rel_sensor_angle) > orig_gauge_angle_max:
        #    ax_sub.text( orig_rel_sensor_angle * np.pi / 180., 2, f'({rel_sensor_angle:.2f}°)', color='#ff7f0e',
        #            ha='left' if orig_rel_sensor_angle < -orig_gauge_angle_max else 'right', va='bottom')
        
        #if abs(orig_rel_pcb_angle) > orig_gauge_angle_max:
        #    ax_sub.text( (orig_rel_pcb_angle + (15 if orig_rel_pcb_angle > 0 else -15)) * np.pi / 180., 1.0, f'({rel_pcb_angle:.2f}°)', color='#2ca02c',
        #            ha='left' if orig_rel_pcb_angle < -orig_gauge_angle_max else 'right', va='bottom')
        
        
        
        ax_sub.annotate('', xy        = (orig_rel_sensor_angle * np.pi / 180., 2),
                        xytext    = (0., -2.5),
                        arrowprops= dict(color    ='#ff7f0e',
                                         arrowstyle="->"),
                    )
        ax_sub.annotate('', xy        = (orig_rel_pcb_angle * np.pi / 180., 1.6),
                        xytext    = (0., -2.5),
                        arrowprops= dict(color    ='#2ca02c',
                                         arrowstyle="->"),
                    )
        
        #    ax_sub.annotate('', xy        = (transfer_factor * 0. * np.pi / 180., 2),
        #                    xytext    = (0., -2.5),
        #                    arrowprops= dict(color    ='k',
        #                                     arrowstyle="->",
        #                                     ),
        #                )
        ax_sub.annotate('', xy        = (transfer_factor * 0.02 * np.pi / 180., 2),
                        xytext    = (transfer_factor * 0.02 * np.pi / 180., 0.),
                        arrowprops= dict(color    ='b',
                                         arrowstyle="-",
                                         linestyle ="dotted"
                                         ),
                    )
        ax_sub.annotate('', xy        = (transfer_factor * -0.02 * np.pi / 180., 2),
                        xytext    = (transfer_factor * -0.02 * np.pi / 180., 0.),
                        arrowprops= dict(color    ='b',
                                         arrowstyle="-",
                                         linestyle ="dotted"
                                         ),
                    )
        ax_sub.annotate('', xy        = (transfer_factor * 0.04 * np.pi / 180., 2),
                        xytext    = (transfer_factor * 0.04 * np.pi / 180., 0.),
                        arrowprops= dict(color    ='r',
                                         arrowstyle="-",
                                         linestyle ="dotted"
                                         ),
                    )
        ax_sub.annotate('', xy        = (transfer_factor * -0.04 * np.pi / 180., 2),
                        xytext    = (transfer_factor * -0.04 * np.pi / 180., 0.),
                        arrowprops= dict(color    ='r',
                                         arrowstyle="-",
                                         linestyle ="dotted"
                 
                                         ),
                    )


    # Outside boundary region
    #node = np.linspace(orig_gauge_angle_max * np.pi / 180., orig_gauge_angle_max * 1.2 * np.pi / 180., 50)
    #ax_sub.fill_between(node, 0, 2, color='r', alpha=0.05)
    #ax_sub.fill_between(-1. * node, 0, 2, color='r', alpha=0.05) ### PINK AREA FOR ANGLE
    #ax_sub.fill_between(-1. * node, 0, 2, color='r', alpha=(0.05/len(List_module_name)))
    
    #print("Check home folder for Output");
    plt.savefig(f'{module_name}_accuracy.png')  # Save first
    plt.show()                                  # Then display
    plt.close()                                 # Finally close


#make_accuracy_plot(
#    module_name = 'RETRY',
#    rel_sensor_X = 0.070,
##    
 #   rel_sensor_Y = -0.180,
#    rel_pcb_X = 0.160,
#    rel_pcb_Y = -0.080,
#    rel_sensor_angle = 0.0065,
#    rel_pcb_angle = 0.1312
#)


if __name__ == "__main__":


    List_module_name = [
        "320MHF1T4SB0019", "320MHF1T4SB0020", "320MHF1T4SB0021", "320MHF1T4SB0022",
        "320MHF1T4SB0023", "320MHF1T4SB0024", "320MHF1T4SB0025", "320MHF1T4SB0026"
    ]
    List_rel_sensor_X = [0.003, 0.017, 0.010, -0.010, 0.023, 0.002, 0.010, -0.006]
    List_rel_sensor_Y = [-0.017, -0.009, -0.005, -0.022, 0.010, -0.018, -0.022, -0.036]
    List_rel_sensor_angle = [-0.001, 0.001, 0.007, 0.003, 0.005, -0.010, 0.006, 0.006]
    List_rel_pcb_X = [0.022, 0.026, 0.020, 0.019, 0.056, 0.016, -0.008, 0.011]
    List_rel_pcb_Y = [-0.028, 0.004, 0.017, 0.001, -0.010, -0.023, 0.044, 0.027]
    List_rel_pcb_angle = [0.076, 0.028, -0.006, -0.004, 0.012, -0.013, 0.016, 0.005]
    
    listA = [List_module_name, List_rel_sensor_X, List_rel_sensor_Y, List_rel_pcb_X, List_rel_pcb_Y, List_rel_sensor_angle, List_rel_pcb_angle]
    make_accuracy_plot(listA);
