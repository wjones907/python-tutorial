import yaml
import pprint

# Sample Yaml File:
# The variable dataMap now contains a dictionary with the tree data. If you print dataMap using PrettyPrint, you will
# get something like:
'''  tree.yaml
{'treeroot': {'branch1': {'branch1-1': {'name': 'Node 1-1'},
    'name': 'Node 1'},
    'branch2': {'branch2-1': {'name': 'Node 2-1'},
    'name': 'Node 2'}}}
'''

"""
    yaml.load()
    yaml.safe_load()
    yaml.load_all()
    yaml.dump()
    stream = file('doc.yaml','w')
    f = open('tree.yaml','r')
        data = yaml.load(f)
    with open('tree.yaml','r') as f:
        data = yaml.load(f)
"""

def open_yaml_file():
    f = open('tree.yaml')
    # use safe_load instead load
    dataMap = yaml.safe_load(f)
    f.close()

def open_yaml_file2():
    #another open method
    import yaml
    with open('tree.yaml', 'r') as f:
        doc = yaml.load(f)


def saving_yaml_file():
    #saving data into a yaml file
    f = open('newtree.yaml', "w")
    yaml.dump(dataMap, f)
    f.close()


def access_yaml_keyvalues():
    # accessing yaml key values
    """
    treeroot:
        branch1: branch1 text
        branch2: branch2 text
    """
    txt = doc["treeroot"]["branch1"]
    print txt
    "branch1 text"

def yaml_dump2():
    # yaml dump
    # The yaml.dump function accepts a Python object and produces a YAML document.

    """
    print yaml.dump({'name': 'Silenthand Olleander', 'race': 'Human',
    ... 'traits': ['ONE_HAND', 'ONE_EYE']})

    name: Silenthand Olleander
    race: Human
    traits: [ONE_HAND, ONE_EYE]
    """
    #dump to a file
    """
    >>> stream = file('document.yaml', 'w')
    >>> yaml.dump(data, stream)    # Write a YAML representation of data to 'document.yaml'.
    >>> print yaml.dump(data)      # Output the document to the screen.
    """

def yaml_loader(filepath):
    """ Loads a yaml file """
    with open(filepath,"r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath,data):
    """ Dumps data to a yamal file """
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

def write_to_yaml_file():
    filepath2 = "test2.yaml"
    data2 = {
        "items": {
            "sword": 100,
            "axe": 80,
            "boots": 40
        }
    }
    yaml_dump(filepath2, data2)

def test_yaml_load():
    filepath = "tree.yaml"

    data = yaml_loader(filepath)

    items = data.get('treeroot')
    for item_name, item_value in items.iteritems():
        print item_name, item_value

def test_yaml_write():
    #write_to_yaml_file()
    print


def read_yaml_file(filepath,rootitem):
    # open file, return data object
    data = yaml_loader(filepath)
    #pprint.pprint(data)
    pprint.pprint(data)
    print(data)
    print 'data[treeroot]',data['treeroot']
    print 'data[treeroot][branch3]', data['treeroot']['branch3']
    print 'data[treeroot][branch2]', data['treeroot']['branch2']
    print 'data[treeroot][branch1]', data['treeroot']['branch1']

    # iterate through the data object
if __name__ == "__main__":
    print 'in test_yaml.py - __name__:',__name__

    read_yaml_file("tree.yaml","treeroot")







