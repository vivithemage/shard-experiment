import sys
import zlib

argument = sys.argv[1]
domain_crc_signed = zlib.crc32(argument)
domain_crc = domain_crc_signed & 0xffffffff
bucket_quantity = 64
bucket_id = domain_crc % bucket_quantity
print(bucket_id)
