import matplotlib.pylab as plt
import uclchem
import os

if not os.path.exists('examples/astrochemistry_test/'):
    os.makedirs('examples/astrochemistry_test/')

out_species = ["O2","CO","H2O"]
param_dict = {
    "endAtFinalDensity": False,#stop at finalTime
    "freefall": False,#don't increase density in freefall
    "initialDens": 1e4, #starting density
    "initialTemp": 10.0,#temperature of gas
    "finalTime": 1.0e7, #final time
    "rout":0.1, #radius of cloud in pc
    "points":1,#Number of gas parcels equally spaced between rin to rout to consider
    "freezeFactor":1.,#Modify freeze out rate of gas parcels by this factor.
    "desorb": True,#Toggles all non-thermal desoprtion processes on or off.
    "zeta":1.,#Cosmic ray ionisation rate as multiple of 1.3e-17 s^{-1}
    "fo":3.34e-04,#Total elemental abundance of O with respect to total H.
    "fc":1.77e-04,#Total elemental abundance of C with respect to total H. 
    "fn":6.18e-05,#Total elemental abundance of N with respect to total H.
    "fhe":0.1,#Total elemental abundance of He with respect to total H.
    "baseAv":10.0, #visual extinction at cloud edge.
    "outputFile": "examples/astrochemistry_test/static-full.dat",#full UCLCHEM output
    "abundSaveFile": "examples/astrochemistry_test/startstatic.dat",#save final abundances to file
}
result = uclchem.model.cloud(param_dict=param_dict,out_species=out_species)
print(result)
result_df=uclchem.analysis.read_output_file("examples/astrochemistry_test/static-full.dat")
conservation=uclchem.analysis.check_element_conservation(result_df,element_list=["H","N","C","O","S"])
print("Percentage change in total abundances:")
print(conservation)

