import pandas
import matplotlib.pyplot as plt
import numpy
import argparse
import scipy

def prepare_data(data: pandas.DataFrame, n: int):
    return data.tail(n)
       

def plot_system(ax0, ax1, data: pandas.DataFrame, column: str, mult: float, label: str='', color: str=''):
    
    mean, std = data[column].mean(), data[column].std()
    ax0.plot(numpy.arange(len(data)) * mult, data[column], 'o', color=color, label='{} ({:.1f} $\\pm$ {:.1f})'.format(label, mean, std))
    
    ax0.set_xlim(0, len(data) * mult)
    
    yspace = numpy.linspace(mean - 3 * std, mean + 3 * std, 300)
    kde = scipy.stats.gaussian_kde(data[column])
    ax1.plot(kde(yspace), yspace, '-')
    
    ax1.plot([0, .75 * kde(yspace).max()], [mean, mean], '-', color=color)
    

parser = argparse.ArgumentParser()
parser.add_argument('inputs', nargs='*')
parser.add_argument('-o', '--output', default='Data_da.pdf')
parser.add_argument('-n', '--names', nargs='*', required=True)
parser.add_argument('-c', '--column', required=True)
parser.add_argument('-x', '--frames', type=int, default=700)
parser.add_argument('-m', '--mx', type=float, default=.05)
parser.add_argument('-y', '--ylabel', default='d')

args = parser.parse_args()

if len(args.names) != len(args.inputs):
    raise Exception('len(annotations) and len(inputs) should match')

figure = plt.figure(figsize=(8, 5))

gs = figure.add_gridspec(1, 2,  width_ratios=(4, 1))

ax0 = figure.add_subplot(gs[0, 0])
ax1 = figure.add_subplot(gs[0, 1], sharey=ax0)

COLORS = ['tab:orange', 'tab:blue', 'tab:green', 'tab:red', 'tab:pink']

for i, (inp, name) in enumerate(zip(args.inputs, args.names)):
    data = prepare_data(pandas.read_csv(inp), args.frames)
    plot_system(ax0, ax1, data, args.column, args.mx, name, color=COLORS[i])

ax0.set_xlabel('time (fs)')
ax0.set_ylabel(args.ylabel)
ax1.tick_params(axis="y", labelleft=False)
ax1.tick_params(axis="x", labelbottom=False)
ax0.legend()

plt.tight_layout()
figure.savefig(args.output)
