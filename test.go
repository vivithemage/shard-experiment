package main

import (
	"fmt"
	"hash/crc32"
)

func main() {
	crc32InUint32 := crc32.ChecksumIEEE([]byte("hello-world"))

	fmt.Println(crc32InUint32)
	//crc32InString := strconv.FormatUint(uint64(crc32InUint32), 16)
	//fmt.Println(crc32InString)
}
