#RiP
import csv
import sys

##########################################################################
#####****************************************************************#####
def VdG_dat2List(File):
    """
    Converts .dat files from VdG RBS into yield list
    INPUTS:
        "FILENAME.dat"
    OUTPUTS:
        Yield list
    HOW TO USE:
        MyYield, MyChannel = VdG_dat2List("MyFile.dat")
    """
    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    ch = []
    y = []
    aux = []
    for i in range(128):
        aux.append(data[i][0].split())
    #print(aux)
    for i in range(len(aux)):
        for k in range(8):
            ch.append(int(8*(i)+k+1)) ## axes in channel
            y.append(float(aux[i][k]))
    
    return y, ch
#####****************************************************************#####
##########################################################################




def VdG_dat2Lists(File):
    """
    Converts .dat files from VdG RBS into yield and channel lists
    INPUTS:
        "FILENAME.dat"
    OUTPUTS:
        Yield and Channel lists
    HOW TO USE:
        MyYield, MyChannel = VdG_dat2Lists("MyFile.dat")
    """
    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    ch = []
    y = []
    aux = []
    for i in range(128):
        aux.append(data[i][0].split())
    #print(aux)
    for i in range(len(aux)):
        for k in range(8):
            ch.append(int(8*(i)+k+1)) ## axes in channel
            y.append(float(aux[i][k]))
    
    return y, ch



def VdG_dat2SIMNRAfile(File):
    """
    Converts .dat files from VdG RBS into yield single list file to be read with SIMNRA
    INPUTS:
        "FILENAME.dat"
    OUTPUTS:
        "FILENAME_SIMNRA.dat
    HOW TO USE:
        VdG_dat2SIMNRAfile(FILENAME)
    """
    outName = str(File)
    Output = open('sortSIMNRA'+outName, 'w')
    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    y = []
    aux = []
    for i in range(128):
        aux.append(data[i][0].split())
    #print(aux)
    for i in range(len(aux)):
        for k in range(8):
            Output.write(str(int(aux[i][k]))+'\n')
    Output.close()
    
    return 'Done'


    

def VdG_dat2file(File):
    """
    Converts .dat files from VdG RBS into yield single list file to be read with SIMNRA
    INPUTS:
        "FILENAME.dat"
    OUTPUTS:
        "FILENAME_SIMNRA.dat
    HOW TO USE:
        VdG_dat2SIMNRAfile(FILENAME)
    """
    outName = str(File)
    Output = open('sort'+outName, 'w')
    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    y = []
    aux = []
    for i in range(128):
        aux.append(data[i][0].split())
    #print(aux)
    for i in range(len(aux)):
        for k in range(8):
            Output.write(str(int(aux[i][k]))+'\n')
    Output.close()
    
    return 'Done'
#############################################################################
#############################################################################


###   Conversitons   ###
VdG_dat2file('RBS1run10.dat')
VdG_dat2file('RBS1run11.dat')
