import hashlib


def md5Experiment(domain_name, total_shards):
  hash_obj = hashlib.md5(b'example.com')
  digest = hash_obj.hexdigest()
  shard_id = int(digest, 16) % total_shards
  
  return shard_id

print("database id: " + str(md5Experiment(b'example.com', 3)))
