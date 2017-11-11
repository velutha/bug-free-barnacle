import os,time,hashlib,json
import pdb

class Block(object):

    def __init__(self, dictionary):

        """
        We're looking for index, timestamp, data, prev_hash, nonce 
        """

        for key, value in dictionary.items():
            setattr(self, key, value)

        if not hasattr(self, 'nonce'):
            # we're thrownin this for generation
            self.nonce = "None"

        if not hasattr(self, "hash"): # in creating the first block, needs to removed in future 
            self.hash = self.create_self_hash()
    
    def header_string(self):
        return str(self.index) + self.prev_hash + self.data + str(self.timestamp) + str(self.nonce)

    def create_self_hash(self):
        sha = hashlib.sha256()
        sha.update(bytes(self.header_string(), 'utf-8'))
        return sha.hexdigest()

    def self_save(self):
        chaindata_dir = 'chaindata'
        index_string = str(self.index).zfill(6)
        filename = "%s/%s.json" % (chaindata_dir, index_string)
        with open(filename, 'w') as block_file:
            json.dump(self.__dict__(), block_file)

    def __dict__(self):
        info = {}
        info["index"] = str(self.index)
        info["timestamp"] = str(self.timestamp)
        info["prev_hash"] = str(self.prev_hash)
        info["hash"] = str(self.hash)
        info["data"] = str(self.data)
        return info

    def __str__(self):
        return "Block<prev_hash: %s, hash: %s" %(self.prev_hash, self.hash)


def create_first_block():
    # index zero and arbitrary previous hash
    block_data = {}
    block_data["index"] = 0
    block_data["timestamp"] = int(time.time()) 
    block_data["data"] = "First block data"
    block_data["prev_hash"] = ""
    block_data["nonce"] = 0 #starting it at 0
    block = Block(block_data)
    return block

if __name__ == "__main__":
# check if chaindata folder exists
    chaindata_dir = "chaindata"
    if not os.path.exists(chaindata_dir):
        # make chaindata dir
        os.mkdir(chaindata_dir)
        # check if dir is empty from just creation of empty befor

    if os.listdir(chaindata_dir) == []:
        # create first block
        first_block = create_first_block()
        first_block.self_save()
