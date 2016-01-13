import os
import inspect
import importlib
from global_vars import available_parts


def grab_parts(main, sub, directory):
    '''
    Given a certain subdirectory, locate all the parts in that directory and
    add them to the required type and subtype.
    '''
    if sub != '':
        partlist = available_parts[main][sub]
        modulebase = '.'.join(['cars.parts', main, sub])
    else:
        partlist = available_parts[main]
        modulebase = '.'.join(['cars.parts', main])

    pcount = 0
    for part in next(os.walk(directory))[1]:
        if part[0] not in ['_', '.']:
            module = importlib.import_module('.'.join([modulebase, part, part]))
            partclass = getattr(module, 'mainclass', None)
            if partclass:
                partlist[partclass.identifier] = partclass
                pcount += 1
    return pcount


def discover():
    '''
    Discover the parts that are available in the system. By doing this in code,
    it allows easy addition of more parts without having to keep a static list
    somewhere. 'Modability'
    '''
    pcount = 0
    pcount += grab_parts('body', 'frame', 'cars/parts/body/frame')
    pcount += grab_parts('body', 'options', 'cars/parts/body/options')
    pcount += grab_parts('drive', 'drivetype', 'cars/parts/drive/drivetype')
    pcount += grab_parts('drive', 'gearbox', 'cars/parts/drive/gearbox')
    pcount += grab_parts('drive', 'options', 'cars/parts/drive/options')
    pcount += grab_parts('engine', 'enginetype',
                         'cars/parts/engine/enginetype')
    pcount += grab_parts('engine', 'head', 'cars/parts/engine/head')
    pcount += grab_parts('engine', 'options', 'cars/parts/engine/options')
    pcount += grab_parts('interior', 'seats', 'cars/parts/interior/seats')
    pcount += grab_parts('interior', 'options', 'cars/parts/interior/options')
    mcount = grab_parts('materials', '', 'cars/parts/materials')
    return pcount, mcount


class Part:
    def __init__(self):
        raise NotImplemented