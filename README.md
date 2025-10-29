# UCSB_HEP_Gantry_Placement_Plotter
Repository serves as the main location for editing the accuracy plot code. 




1. Hexagonal Acc plot Mod - Make Hexagonal Modification of the Make accuracy plot script (try replacing Red square with red hexagon)
#this is for -ANDY
    #    to; ANDY
        hey andy, You'll need to know that the Yellow-Red Hexagonal Border is 0.64mm wide, and the green-yellow hexagonal border is 0.17mm wide. Your replaceing the red, 100um Rectangle with a 640um wide hexagon. and the little blue rectangle with a 170um wide green hexagon. 
    Instead of a static Value: widths should be more of a peicewise function (based on 10/29/25 current numbers from Module Edes Study)
        -yellow_width = -1.96*x + 0.648  [0 -> 0.16]   #    -0.236*x + 0.379 [0.16 -> 0.5]
        -yellow_Height = -2.26*x + 0.748  [0 -> 0.16]   #   -.0273*x + 0.438  [0.16 -> 0.5]
        -green_width = -1.89*x + 0.185   [0 -> 0.16]   #
        -green_height =  -2.18*x + 0.214  [0 -> 0.16]   #



2. Get PGConnect Working / Connect to LocalDB, Pull Info from Module Inspect, Proto Inspect, and Others
    
3. Make GUI for selecting Groups of Modules from Postgres

4. Make Automated Histogram To Acompany the Placement Statistics 