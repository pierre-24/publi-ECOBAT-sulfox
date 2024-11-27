import pandas
import matplotlib.pyplot as plt
import numpy
import argparse
import scipy

def prepare_data(data: pandas.DataFrame):
    return data
       

def plot_system(ax, data: pandas.DataFrame, limits: tuple = (0, 10), label: str='', color: str='', distance: int = 15, shiftmax: tuple=(10, 0), shiftmin=(10,-10)):
    ax.plot(data['r'], data['rdf'], '-', label=label, color=color)
    
    maxima = scipy.signal.find_peaks(data['rdf'], distance=distance, prominence=2)
    minima = scipy.signal.argrelmin(data['rdf'].to_numpy(), order=distance)
    
    ax.text(.02, .9, label, transform=ax.transAxes, fontsize=12)
    
    #ax.plot(data['r'][maxima[0]], data['rdf'][maxima[0]], 'o', color=color)
    #ax.plot(data['r'][minima[0]], data['rdf'][minima[0]], 'x', color=color)
    for i in maxima[0]:
        ax.annotate(
            '{:.2f} ({:.1f})'.format(data['r'][i], data['cdf'][i]), 
            (data['r'][i], data['rdf'][i]), 
            shiftmax, 
            textcoords='offset pixels', 
            arrowprops={'color': color, 'arrowstyle': '->'}, 
            color=color,
            ha='right'
        )
    for i in minima[0]:
        ax.annotate(
            '{:.2f} ({:.1f})'.format(data['r'][i], data['cdf'][i]), 
            (data['r'][i], data['rdf'][i]), 
            shiftmin, 
            textcoords='offset pixels', 
            arrowprops={'color': color, 'arrowstyle': '->'}, 
            color=color,
            va='top',
            ha='right'
        )
    ax.set_xlim(*limits)


def get_limits(inp: str):
    try:
        limits = [float(x) for x in inp.split(':')]
    except ValueError:
        raise argparse.ArgumentTypeError('`limits` must contain float')
    
    if len(limits) != 2:
        raise argparse.ArgumentTypeError('`limits` must contain 2 elements')
        
    return limits

def get_annotations(inp: str):
    pre_annotations = inp.split(',')
    annotations = []
    
    for annotation in pre_annotations:
        try:
            limits = [float(x) for x in annotation.split(':')]
        except ValueError:
            raise argparse.ArgumentTypeError('annotation must contain float')
    
        if len(limits) != 3:
            raise argparse.ArgumentTypeError('annotation must contain 3 elements')
        
        annotations.append(limits)
        
    return annotations

parser = argparse.ArgumentParser()
parser.add_argument('inputs', nargs='*')
parser.add_argument('-l', '--limits', default='0:10', type=get_limits)
parser.add_argument('-o', '--output', default='Data_rdf.pdf')
parser.add_argument('-n', '--names', nargs='*', required=True)

args = parser.parse_args()

if len(args.names) != len(args.inputs):
    raise Exception('len(annotations) and len(inputs) should match')

figure = plt.figure(figsize=(9, 3 * len(args.inputs)))
axes = figure.subplots(len(args.inputs), sharex=True)

for i, (ax, inp, name) in enumerate(zip(axes, args.inputs, args.names)):
    data = prepare_data(pandas.read_csv(inp))
    plot_system(ax, data, limits=args.limits, label=name, color='k', shiftmax=(-20, 5), shiftmin=(-20, -5))

axes[-1].set_xlabel('r (Å)')
[ax.set_ylabel('g(r)') for ax in axes.flatten()]

plt.tight_layout()
figure.savefig(args.output)
