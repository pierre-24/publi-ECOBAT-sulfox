import pandas
import matplotlib.pyplot as plt
import numpy
import argparse

def prepare_data(data: pandas.DataFrame):
    return data
        

def plot_system(ax, data: pandas.DataFrame, annotations: list = [], limits: tuple = (0, 10), label: str='', color: str=''):
    ax.plot(data['r'], data['rdf'], '-', label=label, color=color)
    ax.set_xlim(*limits)
    
    max_rdf = data['rdf'].max()
    
    for ab,ae,x in annotations:
        subdata = data[(data['r'] >= ab) & (data['r'] <= ae)]
        max_ = data.iloc[subdata.idxmax()['rdf']]
        ax.plot(max_['r'], max_['rdf'], 'o', color=color)
        ax.annotate('{:.2f}'.format(max_['r']), (max_['r'], max_['rdf']), color=color, textcoords='offset pixels', xytext=(0, 5), ha='center', fontsize=8)
        ax.plot([ab, ae], [max_['rdf'] * x] * 2, '-', color=color, linewidth=.7)
        ax.plot([ab, ab], [0, max_['rdf'] * x], '-', color=color, linewidth=.7)
        ax.plot([ae, ae], [max_['rdf'] * x - max_rdf * .05, max_['rdf'] * x + max_rdf * .05], '-', color=color, linewidth=.7)
        ax.annotate('N={:.2f}'.format(subdata.iloc[-1]['cdf'] - subdata.iloc[0]['cdf']), (ae, max_['rdf'] * x), color=color, textcoords='offset pixels', xytext=(5, 0), ha='left', va='center')
        


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
parser.add_argument('-a', '--annotations', nargs='*', required=True, type=get_annotations)
parser.add_argument('-n', '--names', nargs='*', required=True)

args = parser.parse_args()

if len(args.annotations) != len(args.inputs):
    raise Exception('len(annotations) and len(inputs) should match')

if len(args.names) != len(args.inputs):
    raise Exception('len(annotations) and len(inputs) should match')

figure = plt.figure(figsize=(7, 5))
ax1 = figure.subplots()

COLORS = ['red', 'green', 'blue']

for i, (inp, name, annotations) in enumerate(zip(args.inputs, args.names, args.annotations)):
    data = prepare_data(pandas.read_csv(inp))
    plot_system(ax1, data, annotations=annotations, limits=args.limits, label=name, color=COLORS[i])

ax1.set_xlabel('r (Å)')
ax1.set_ylabel('g(r)')
ax1.legend()

plt.tight_layout()
figure.savefig(args.output)
