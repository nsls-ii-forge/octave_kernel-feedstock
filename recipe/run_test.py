import json
import os
import sys

specfile = os.path.join(os.environ['PREFIX'], 'share', 'jupyter', 'kernels',
                        'octave', 'kernel.json')
with open(specfile, 'r') as fh:
    spec = json.load(fh)


if spec['argv'][0] != 'python':
    raise ValueError('The specfile seems to have the wrong executable. \n'
                     'Specfile: {}; Expected: {};'
                     ''.format(spec['argv'][0], 'python'))
