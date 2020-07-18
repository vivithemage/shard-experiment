# shard-experiment


Testing out hash functions and evaluating whether they are distributed evenly when a modulus is
applied to them.

CRC32 was tried first but this does not seem to good use of the function as it was not designed for
this purpose. In addition to this, there may be more even distribution using an MD5 hash instead.

For more details, please see: https://blog.vixre.co.uk/evenly-distributing-data-on-a-group-of-mysql-databases/

ref: https://web.archive.org/web/20120722074858/http://bretm.home.comcast.net/~bretm/hash/8.html
