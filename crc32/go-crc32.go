package main

import (
	"os"
	"fmt"
	"hash/crc32"
)

var (
	bucket_id uint32
	bucket_quantity uint32
)

func main() {
	argument := os.Args[1]
	crc32InUint32 := crc32.ChecksumIEEE([]byte(argument))

	bucket_quantity = 32
	bucket_id = crc32InUint32 % bucket_quantity

	fmt.Println(bucket_id)
}
