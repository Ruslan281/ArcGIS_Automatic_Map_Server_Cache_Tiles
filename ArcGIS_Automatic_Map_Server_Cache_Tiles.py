# Created by Ruslan Huseynov
import sys
import os
import arcpy
import datetime
import random
import ConfigParser
import arcpy
from collections import OrderedDict
import time
import traceback
import string


##########################################----Məlumatlar-----###################################################
##########################################----Məlumatlar-----###################################################                                                                                                              
                                                                                                             ###
# Nümunə  :  workspace = r'C:\Ruslan\KTB\Desktop\Test\Test.gdb'                                              ###                                                                                                           ##                                                                                                                                                                                                                         
workspace ="C:/Users/RuslanHu/Desktop/Auto/TEST_DATA.gdb"                                                    ###
                                                                                                             ###
# Nümunə  : connectionFile = r"C:\Ruslan\<username>\AppData\Roaming\ESRI\Desktop10.1\ArcCatalog"             ###
connectionFile =r'C:\Users\RuslanHu\AppData\Roaming\ESRI\Desktop10.6\ArcCatalog'                             ###
                                                                                                             ###
# Nümunə  : server = "arcgis on MyServer_6080 (admin)"                                                       ###
server = "arcgis on 10.0.0.0_6080 (admin)\TEST"                                                             ###
                                                                                                             ###
# Nümunə  : serviceName = "Ruslan.MapServer"                                                                 ###
serviceName = "cache_service.MapServer"                                                                      ###
                                                                                                             ###
inputService = connectionFile + "\\" + server + "\\" + serviceName    # Not touch                            ###
                                                                                                             ###
                                                                                                             ###
scales = [144447.638572,72223.819286,36111.909643,18055.954822,                                              ###
          9027.977411,4513.988705,                                                                           ###
          2256.994353,1128.497176,564.248588,282.124294]     # Dey    # Deyisilecekse deyisdirilsin ###      ###
                                                                                                             ###
numOfCachingServiceInstances = 10         # Not touch                                                        ###
                                                                                                             ###
updateMode = "RECREATE_ALL_TILES"         # Not touch                                                        ###
                                                                                                             ###
waitForJobCompletion = "WAIT"             # Not touch                                                        ###
                                                                                                             ### 
updateExtents = ""                        # Not touch                                                        ###
                                                                                                             ###
################################################################################################################
################################################################################################################


def Control():

    arcpy.env.workspace =workspace
    
    print("---> Calisma alani teyin edildi...")

    

    arcpy.env.scratchWorkspace ="c:/projects/Scratch/scratch.gdb"

    for i in range(2):
        print(">")

        
    time.sleep(2)
    
    print("---> Scratch elave edildi...")

    time.sleep(2)

    start_time ='2021-01-15 15:42:00'  # Datada hansi sabit vaxtirsa o goturulecek

    start_timee = datetime.datetime.strptime(start_time,'%Y-%m-%d %H:%M:%S')

    difference=start_timee.strftime('%Y-%m-%d %H:%M:%S')


    

    



#######################################   test layer   ###########################################


    for i in range(2):
        print(">")

    time.sleep(2)
    
    print("---> test layerleri uzerinde son deyisikler kontrol edilir...") ## Daxil edilen layda deyisiklikler edilecek
    
    arcpy.MakeFeatureLayer_management("test", "test_layer","","","")
    
    SQL = "created_date >= date" + "'"+difference+"'" + "OR  last_edited_date >= date" + "'"+difference+"'"

    arcpy.SelectLayerByAttribute_management("test_layer","NEW_SELECTION", SQL)
    
    arcpy.Buffer_analysis('test_layer', 'test_Buffer','1 Meters', 'FULL', 'ROUND', 'NONE', '#')
    
    arcpy.SelectLayerByAttribute_management('test_layer', 'CLEAR_SELECTION', '#')

    for i in range(2):
        print(">")

    time.sleep(2)

    
    print("---> Eger test layerleri uzerinde deyisiklik varsa 1 metr buffer verildi...")
    
#######################################   point   ###########################################

    for i in range(2):
        print(">")

    time.sleep(2)

    print("---> Pointler uzerinde son deyisikler kontrol edilir...")
    
    arcpy.MakeFeatureLayer_management("test", "Point","","","")
    
    SQL = "created_date >= date" + "'"+difference+"'" + "OR  last_edited_date >= date" + "'"+difference+"'"

    arcpy.SelectLayerByAttribute_management("Point","NEW_SELECTION", SQL)
    
    arcpy.Buffer_analysis('Point', 'Point_Buffer','1 Meters', 'FULL', 'ROUND', 'NONE', '#')
    
    arcpy.SelectLayerByAttribute_management('Point', 'CLEAR_SELECTION', '#')

    for i in range(2):
        print(">")

    time.sleep(2)

    
    print("---> Eger Point layerleri uzerinde deyisiklik varsa 1 metr buffer verildi...")

#######################################   ACT_BUILDING   ###########################################

    for i in range(2):
        print(">")

    time.sleep(2)

    print("---> layer uzerinde son deyisikler kontrol edilir...")

    arcpy.MakeFeatureLayer_management("test", "Building","","","")
    
    SQL = "created_date >= date" + "'"+difference+"'" + "OR  last_edited_date >= date" + "'"+difference+"'"

    arcpy.SelectLayerByAttribute_management("Building","NEW_SELECTION", SQL)
    
    arcpy.Buffer_analysis('Building', 'Building_Buffer','1 Meters', 'FULL', 'ROUND', 'NONE', '#')
    
    arcpy.SelectLayerByAttribute_management('Building', 'CLEAR_SELECTION', '#')

    for i in range(2):
        print(">")

    time.sleep(2)

    print("---> Eger layer uzerinde deyisiklik varsa 1 metr buffer verildi...")


#######################################   ACT_AUXILIARY_BUILDING   ###########################################

    for i in range(2):
        print(">")

    time.sleep(2)

    print("---> layer uzerinde son deyisikler kontrol edilir...")


    arcpy.MakeFeatureLayer_management("EXAMPLE_LAYER", "Komekci","","","")
    
    SQL = "created_date >= date" + "'"+difference+"'" + "OR  last_edited_date >= date" + "'"+difference+"'"

    arcpy.SelectLayerByAttribute_management("Komekci","NEW_SELECTION", SQL)
    
    arcpy.Buffer_analysis('Komekci', 'Komekci_Buffer','1 Meters', 'FULL', 'ROUND', 'NONE', '#')
    
    arcpy.SelectLayerByAttribute_management('Komekci', 'CLEAR_SELECTION', '#')

    for i in range(2):
        print(">")

    time.sleep(2)

    print("---> Eger layer uzerinde deyisiklik varsa 1 metr buffer verildi...")


    arcpy.Union_analysis('Building_Buffer #;Komekci_Buffer #;test_Buffer #;Point_Buffer #',
                         "Umumi_Buffer", 'ALL', '#', 'GAPS')

    


    for i in range(2):
        print(">")

    time.sleep(2)
    
    print("---> Layerler uzerinde olan deyisikliklerden alinmis bufferler 'Umumi_Buffer' olaraq birlesdirildi")


        

########################################-----------Cache-----------########################################
def Cache():

    areaOfInterest = "Umumi_Buffer"
    
    currentTime = datetime.datetime.now()
    
    arg1 = currentTime.strftime("%H-%M")
    
    arg2 = currentTime.strftime("%Y-%m-%d %H:%M")
    
    filee = (r'C:\Users\RuslanHu\Desktop\Kontrol_Cache_%s.txt' % arg1)

    report = open(filee,'w')

    try:
        starttime = time.clock()

        for i in range(2):
            print(">")

        time.sleep(2)

        print("---> 'Umumi_Buffer'- a gore  CacheTiles(kesleme) ise salindi...")

        
    
        result = arcpy.ManageMapServerCacheTiles_server(inputService, scales,
                                                    updateMode,
                                                    numOfCachingServiceInstances,
                                                    areaOfInterest, updateExtents,
                                                    waitForJobCompletion)


        finishtime = time.clock()

        elapsedtime = finishtime - starttime

        while result.status < 4:
            time.sleep(0.2)
        resultValue = result.getMessages()
    
        report.write ("Yerine yetirildi " + str(resultValue))



    except Exception, e:
        
        tb = sys.exc_info()[2]
        
        report.write("Xeta bas verdi \n" "Line %i" % tb.tb_lineno)
        
        report.write(e.message)

    
    report.close()


    

    
    for i in range(2):
        print(">")

    time.sleep(2)
    
    
    print("---> Cache Tiles ugurla yerine yetirildi")

    for i in range(2):
        print(">")

    time.sleep(2)
        
    print("---> Etrafli melumat ucun yaradilan text faylini kontrol edin")

    arcpy.Delete_management('test_Buffer', '#')
    arcpy.Delete_management('Point_Buffer', '#')
    arcpy.Delete_management('Building_Buffer', '#')
    arcpy.Delete_management('Komekci_Buffer', '#')
    


if __name__ == "__main__":

    Control()
    Cache()
