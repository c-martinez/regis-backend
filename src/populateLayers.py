import json

from datahandler import LayerDataManager


if __name__ == "__main__":
    layerManager = LayerDataManager()

    defsFile = 'layerdefinitions.json'
    print('Loading layers from ' + defsFile)
    defs = json.loads(open(defsFile, 'r').read())
    for layer in defs['layers']:
        print('  > Inserting layer: ' + layer['name'])
        layerManager.saveLayer(layer)
    print('Done.')
