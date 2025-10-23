# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:24:38 2024

@author: hep
"""
import psycopg2

def Get_PG_Info_By_Name(proto_name_list, stage):
    #print("Get_PG_Info_By_Name", proto_name_list, stage)
    results = []
    #print("attempting pull...")

    conn = psycopg2.connect(database="hgcdb",
                            host="gut.physics.ucsb.edu",
                            user="postgres",
                            password="hepuser",
                            port="5432")
    
    cursor = conn.cursor()
    
    # Create a placeholder for each name in the list
    format_strings = ','.join(['%s'] * len(proto_name_list))
    
    if stage == 'module':
        #print("attempting M pull")
        cursor.execute(f'SELECT module_name, x_offset_mu, y_offset_mu, ang_offset_deg FROM module_inspect WHERE module_name IN ({format_strings})', tuple(proto_name_list))
    elif stage == 'protomodule':
        #print("attempting PM pull")
        cursor.execute(f'SELECT proto_name, x_offset_mu, y_offset_mu, ang_offset_deg FROM proto_inspect WHERE proto_name IN ({format_strings})', tuple(proto_name_list))
    else:
        print('ERROR: pg connect did not recive comp_type data')
    rows = cursor.fetchall()

    if not rows:
        results.append(["No data found for the given module names", f"module names: {proto_name_list}"])
    else:
        for row in rows:
            proto_name, x_offset_mu, y_offset_mu, ang_offset_deg = row
            results.append([proto_name, x_offset_mu, y_offset_mu, ang_offset_deg])
    
    cursor.close()
    conn.close()
    #except Exception as e:
        #results.append(["Error", str(e)])

    return results

# Example usage
##result_list = Get_PG_Info_By_Name(['testcomponent_22491104'], 'protomodule')
#for item in result_list:
#    print(item)
