import hashlib
import sys

def md5Experiment(domain_name, total_shards):
  hash_obj = hashlib.md5(domain_name)
  digest = hash_obj.hexdigest()
  shard_id = int(digest, 16) % total_shards
  
  return shard_id

argument = str.encode(sys.argv[1])
print(str(md5Experiment(argument, 32)))
