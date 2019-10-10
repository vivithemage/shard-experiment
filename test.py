import zlib

domain_crc_signed = zlib.crc32('hello-world')
domain_crc = domain_crc_signed & 0xffffffff
print(domain_crc)
