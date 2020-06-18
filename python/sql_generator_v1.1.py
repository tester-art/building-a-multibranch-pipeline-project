import os
import argparse

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--opp", help="opp",
                    action="store_true")
parser.add_argument("--user", help="user",
                    action="store_true")
parser.add_argument("-o", "--output", help="Directs the output to a name of your choice")
args = parser.parse_args()

with open("input.csv") as f:
    file = open(args.output, "w")
    for line in f:
        lst = line.split(",")
        l0_tmp = lst[0]
        l1_tmp = lst[1]
        L2 = l0_tmp.replace("-", "").replace(".", "_").split('@')[0].upper()
        wh = l1_tmp.split('_')[1] + "_WH"
        print(lst[0])
        if args.user:
            file.write('USE ROLE SECURITYADMIN;\nCREATE USER ' + '"' +lst[0]+ '"        '        + 'PASSWORD = ' + "''" + ' DEFAULT_ROLE = ' +  '"' + lst[1].strip() + '"' + ' DEFAULT_WAREHOUSE = ' + wh + ';\nGRANT ROLE ' + '"' + lst[1].strip() + '"' + ' TO USER ' + '"' + lst[0] + '"' + ';\n\n')
        elif args.opp:
            file.write('USE ROLE SYSADMIN;\n\nDROP SCHEMA IF EXISTS OPP.OPP_' + L2 +';\nCREATE TRANSIENT SCHEMA OPP.OPP_' + L2 + ';\n\nUSE ROLE SECURITYADMIN;\n\nCREATE ROLE OPP_' + L2 + ';\nGRANT ROLE "' + lst[1].strip() + '"  TO ROLE OPP_' + L2 + ';\nGRANT USAGE ON DATABASE OPP                            TO ROLE OPP_' + L2 + ';\nGRANT USAGE ON SCHEMA OPP.OPP_' + L2 + '             TO ROLE OPP_' + L2 + ';\nGRANT ALL ON SCHEMA OPP.OPP_' + L2 + '         TO ROLE OPP_' + L2 + ';\nGRANT ALL ON SCHEMA OPP.OPP_' + L2 + '         TO ROLE LOCAL_FCT_ADMINISTRATOR' + ';\nGRANT ROLE OPP_' + L2 + '                      TO USER "' + lst[0] + '";\n' + '\n')
        else:
            if len(lst) > 2:
                file.write('USE ROLE SECURITYADMIN;\nCREATE USER ' + '"' +lst[0]+ '"        '        + 'PASSWORD = ' + "''" + ' DEFAULT_ROLE = ' +  '"' + lst[1].strip() + '"' + ' DEFAULT_WAREHOUSE = ' + wh + ';\nGRANT ROLE ' + '"' + lst[1].strip() + '"' + ' TO USER ' + '"' + lst[0] + '"' + ';\n\nUSE ROLE SYSADMIN;\n\nDROP SCHEMA IF EXISTS OPP.OPP_' + L2 +';\nCREATE TRANSIENT SCHEMA OPP.OPP_' + L2 + ';\n\nUSE ROLE SECURITYADMIN;\n\nCREATE ROLE OPP_' + L2 + ';\nGRANT ROLE "' + lst[1].strip() + '"  TO ROLE OPP_' + L2 + ';\nGRANT USAGE ON DATABASE OPP                            TO ROLE OPP_' + L2 + ';\nGRANT USAGE ON SCHEMA OPP.OPP_' + L2 + '             TO ROLE OPP_' + L2 + ';\nGRANT ALL ON SCHEMA OPP.OPP_' + L2 + '         TO ROLE OPP_' + L2 + ';\nGRANT ALL ON SCHEMA OPP.OPP_' + L2 + '         TO ROLE LOCAL_FCT_ADMINISTRATOR' + ';\nGRANT ROLE OPP_' + L2 + '                      TO USER "' + lst[0] + '";\n' + 'GRANT ROLE ' + lst[2].strip() + '                      TO USER "' + lst[0] + '";\n' + '\n')
            else:
                file.write('USE ROLE SECURITYADMIN;\nCREATE USER ' + '"' +lst[0]+ '"        '        + 'PASSWORD = ' + "''" + ' DEFAULT_ROLE = ' +  '"' + lst[1].strip() + '"' + ' DEFAULT_WAREHOUSE = ' + wh + ';\nGRANT ROLE ' + '"' + lst[1].strip() + '"' + ' TO USER ' + '"' + lst[0] + '"' + ';\n\nUSE ROLE SYSADMIN;\n\nDROP SCHEMA IF EXISTS OPP.OPP_' + L2 +';\nCREATE TRANSIENT SCHEMA OPP.OPP_' + L2 + ';\n\nUSE ROLE SECURITYADMIN;\n\nCREATE ROLE OPP_' + L2 + ';\nGRANT ROLE "' + lst[1].strip() + '"  TO ROLE OPP_' + L2 + ';\nGRANT USAGE ON DATABASE OPP                            TO ROLE OPP_' + L2 + ';\nGRANT USAGE ON SCHEMA OPP.OPP_' + L2 + '             TO ROLE OPP_' + L2 + ';\nGRANT ALL ON SCHEMA OPP.OPP_' + L2 + '         TO ROLE OPP_' + L2 + ';\nGRANT ALL ON SCHEMA OPP.OPP_' + L2 + '         TO ROLE LOCAL_FCT_ADMINISTRATOR' + ';\nGRANT ROLE OPP_' + L2 + '                      TO USER "' + lst[0] + '";\n' + '\n')     
file.close()
