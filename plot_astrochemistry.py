import matplotlib.pylab as plt
import uclchem
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('name', type=str, nargs='+') #Put frequency in GHz on command line                                               
args=parser.parse_args()

result_df=uclchem.analysis.read_output_file("examples/astrochemistry_test/static-full.dat")
print(result_df.head())
species = []
for i in range(len(args.name)-1):
    species.append(str(args.name[i]))

fig,ax=uclchem.analysis.create_abundance_plot(result_df,species,figsize=(6,6))
ax.set(xscale='log',yscale='log',ylim=(1e-11,1e-3),xlim=(10,1e7))
if args.name[-1]=='plot':
    ax.hlines(3e-9, 10,1e7,colors='k')
    ax.annotate('O$_2$',xy=(20,5e-9),color='k')
    ax.hlines(1e-9,10,1e7,colors='k')
    ax.annotate('H$_2$O',xy=(20,1.5e-9),color='k')
plt.savefig('evolution.png')
