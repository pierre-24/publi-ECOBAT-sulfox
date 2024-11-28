import pandas
import matplotlib.pyplot as plt
import numpy
import argparse
import scipy

def prepare_data(data: pandas.DataFrame, n: int):
    return data.tail(n)
       

def plot_system(ax, data: pandas.DataFrame, column: str, position: int, label: str='', color: str=''):
    
    mean, std = data[column].mean(), data[column].std()
    
    vp = ax.violinplot(data[column], [position, ], showmeans=True, quantiles=[.25,.75])
    vp['bodies'][0].set_facecolor(color)
    for p in ['cbars', 'cmins', 'cmaxes', 'cmeans', 'cquantiles']:
        vp[p].set_edgecolors(color)
    
    ax.text(
        position, 
        data[column].min() - .5 if position % 2 == 0 else data[column].max() + .5, 
        '{}\n{:.2f} $\\pm$ {:.2f}'.format(label, mean, std), 
        color=color, 
        ha='center', va='top' if position % 2 == 0 else 'bottom'
    )
    

parser = argparse.ArgumentParser()
parser.add_argument('inputs', nargs='*')
parser.add_argument('-o', '--output', default='Data_da.pdf')
parser.add_argument('-n', '--names', nargs='*', required=True)
parser.add_argument('-c', '--column', required=True)
parser.add_argument('-x', '--frames', type=int, default=700)
parser.add_argument('-y', '--ylabel', default='d')

args = parser.parse_args()

if len(args.names) != len(args.inputs):
    raise Exception('len(annotations) and len(inputs) should match')

figure = plt.figure(figsize=(8, 5))

ax = figure.subplots()

COLORS = ['tab:orange', 'tab:blue', 'tab:green', 'tab:red', 'tab:pink']

for i, (inp, name) in enumerate(zip(args.inputs, args.names)):
    data = prepare_data(pandas.read_csv(inp), args.frames)
    plot_system(ax, data, args.column, i, name, color=COLORS[i])

ax.set_ylabel(args.ylabel)
ax.tick_params('x', bottom=False, labelbottom=False)

plt.tight_layout()
figure.savefig(args.output)
