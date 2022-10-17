package main

import (
	"bytes"
	"fmt"
	"log"

	"github.com/google/gopacket"
	"github.com/google/gopacket/pcap"
)

var DevName = "lo"
var Found = false

func main() {
	devices, err := pcap.FindAllDevs()
	if err != nil {
		log.Panicln("unable to fetch network interfaces...")
	}

	for _, ifDev := range devices {
		if ifDev.Name == DevName {
			Found = true
		}
	}

	if !Found {
		log.Panicln("desired device not found...")
	}

	handle, err := pcap.OpenLive(DevName, 1600, false, pcap.BlockForever)
	if err != nil {
		fmt.Print(err)
		log.Panicln("unable to open handle on the device")
	}
	defer handle.Close()

	if err := handle.SetBPFFilter("tcp and port 21"); err != nil {
		log.Panicln(err)
	}

	source := gopacket.NewPacketSource(handle, handle.LinkType())
	for packet := range source.Packets() {
		appLayer := packet.ApplicationLayer()
		if appLayer == nil {
			continue
		}
		data := appLayer.Payload()
		if bytes.Contains(data, []byte("USER")) || bytes.Contains(data, []byte("PASS")) {
			fmt.Println(string(data))
		}
		fmt.Println(packet)
	}
}
