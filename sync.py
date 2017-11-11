import os,json
from block import Block

def sync():
    node_blocks = []
    # we're assuming that the folder and at lease initial block exists
    chaindata_dir = 'chaindata'
    if os.path.exists(chaindata_dir):
        for filename in os.listdir(chaindata_dir):
            if filename.endswith(".json"): #.DS_STORE sometimes breaks things
                filepath = '%s/%s' % (chaindata_dir, filename)
                with open(filepath, "r") as block_file:
                    block_info = json.load(block_file)
                    block_object = Block(block_info)
                    node_blocks.append(block_object)
    return node_blocks
