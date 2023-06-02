from timeit import default_timer as timer
from typing import Counter
from enum import Enum
from math import prod

lines = str()
with open('input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

class Packet:
	class PacketType(Enum):
		sum = 0
		product = 1
		minimum = 2
		maximum = 3
		literal = 4
		greaterThan = 5
		lessThan = 6
		equalTo = 7

	type = -1
	version = -1
	lengthTypeID = -1 # 0 or 1.  0 = 15 bits represent # bits, 1 = 11 bits represent # packets
	rawSubData = ''
	subPackets = []
	value = -1

	def __init__(self):
		self.subPackets = []

	def getValue(self):
		if self.value == -1: # only calculate if we haven't already calculated
			values = [sp.getValue() for sp in self.subPackets]
			if self.type == Packet.PacketType.sum:
				self.value = sum(values)
			elif self.type == Packet.PacketType.product:
				self.value = prod(values)
			elif self.type == Packet.PacketType.minimum:
				self.value = min(values)
			elif self.type == Packet.PacketType.maximum:
				self.value = max(values)
			elif self.type == Packet.PacketType.greaterThan:
				self.value = 1 if values[0] > values[1] else 0
			elif self.type == Packet.PacketType.lessThan:
				self.value = 1 if values[0] < values[1] else 0
			elif self.type == Packet.PacketType.equalTo:
				self.value = 1 if values[0] == values[1] else 0
		return self.value


# Pass the raw, original binary data to this
def packetsFromBinary(binData):
	i = 0
	packet = Packet()
	while i < len(binData):
		count = Counter(binData[i:])
		if len(binData) - i == count['0']:
			break
		packet.version = int(binData[i:i+3],2)
		i += 3
		packet.type = Packet.PacketType(int(binData[i:i+3],2))
		i += 3
		if packet.type == Packet.PacketType.literal: # literal value
			pass
		else: # operator command
			packet.lengthTypeID = int(binData[i], 2)
			i += 1
			if packet.lengthTypeID == 0:
				numSubBits = int(binData[i:i+15], 2)
				i += 15
				sp, bitsProcessed = getSubPackets(binData[i:], numBits = numSubBits)
				packet.subPackets.extend(sp)
				i += bitsProcessed
			else:
				numSubPackets = int(binData[i:i+11], 2)
				i += 11
				sp, bitsProcessed = getSubPackets(binData[i:], numPackets = numSubPackets)
				packet.subPackets.extend(sp)
				i += bitsProcessed

	return packet

# Given binary data and either the number of bits to corral into sub packets or the number of sub packets to corral, return a list of those packets
def getSubPackets(binData, numBits = -1, numPackets = -1):
	packets = []
	if (numBits == -1 and numPackets == -1) or (numBits != -1 and numPackets != -1):
		raise Exception("Must provide EITHER numBits OR numPackets")
	elif numBits != -1:
		subBitsProcessed = 0
		i = 0
		while subBitsProcessed < numBits:
			newPacket = Packet()
			newPacket.version = int(binData[i:i+3], 2)
			i += 3
			newPacket.type = Packet.PacketType(int(binData[i:i+3], 2))
			i += 3

			if newPacket.type == Packet.PacketType.literal:
				lastNybble = False
				fullData = ''
				while not lastNybble:
					prefix = int(binData[i], 2)
					i += 1
					if prefix == 0: lastNybble = True
					fullData += binData[i:i+4]
					i += 4
				newPacket.value = int(fullData, 2)

			else:
				newPacket.lengthTypeID = int(binData[i], 2)
				i += 1
				if newPacket.lengthTypeID == 0:
					numSubBits = int(binData[i:i+15], 2)
					i += 15
					sp, bitsProcessed = getSubPackets(binData[i:], numBits = numSubBits)
					newPacket.subPackets.extend(sp)
					i += bitsProcessed
				else:
					numSubPackets = int(binData[i:i+11], 2)
					i += 11
					sp, bitsProcessed = getSubPackets(binData[i:], numPackets = numSubPackets)
					newPacket.subPackets.extend(sp)
					i += bitsProcessed

			#Finished processing this sub-packet.  Add it to the list and increment count
			packets.append(newPacket)
			subBitsProcessed = i

		#Return the list of sub packets we processed, along with i, which is how far ahead in the binary Data the calling code will need to jump
		return packets, i

	elif numPackets != -1:
		i = 0
		subPacketsProcessed = 0
		while subPacketsProcessed < numPackets:
			newPacket = Packet()
			newPacket.version = int(binData[i:i+3], 2)
			i += 3
			newPacket.type = Packet.PacketType(int(binData[i:i+3], 2))
			i += 3

			if newPacket.type == Packet.PacketType.literal:
				lastNybble = False
				fullData = ''
				while not lastNybble:
					prefix = int(binData[i], 2)
					i += 1
					if prefix == 0: lastNybble = True
					fullData += binData[i:i+4]
					i += 4
				newPacket.value = int(fullData, 2)

			else:
				newPacket.lengthTypeID = int(binData[i], 2)
				i += 1
				if newPacket.lengthTypeID == 0:
					numSubBits = int(binData[i:i+15], 2)
					i += 15
					sp, bitsProcessed = getSubPackets(binData[i:], numBits = numSubBits)
					newPacket.subPackets.extend(sp)
					i += bitsProcessed
				else:
					numSubPackets = int(binData[i:i+11], 2)
					i += 11
					sp, bitsProcessed = getSubPackets(binData[i:], numPackets = numSubPackets)
					newPacket.subPackets.extend(sp)
					i += bitsProcessed

			#Finished processing this sub-packet.  Add it to the list and increment count
			packets.append(newPacket)
			subPacketsProcessed += 1

		#Return the list of sub packets we processed, along with i, which is how far ahead in the binary Data the calling code will need to jump
		return packets, i


# Recursively sum version numbers of a list of packets and their sub packets
def sumVersionNums(packets):
	versionSum = 0
	for packet in packets:
		versionSum += packet.version
		if len(packet.subPackets) > 0:
			versionSum += sumVersionNums(packet.subPackets)
	return versionSum



def part1(lines):
	#input is a single line
	binData = bin(int(lines[0], 16))[2:]
	binData = binData.zfill(len(lines[0] * 4)) #Leading zeros wlil get truncated by bin().  Add them back here
	packet = packetsFromBinary(binData) #there is always a single outer packet, not multiple (although it probably contains many sub packets)
	return packet

def part2(packet):
	return packet.getValue()

start = timer()
packet = part1(lines)
p1 = sumVersionNums([packet])
end = timer()
print("Part 1:", p1)
print("Time (msec):", (end - start) * 1000)
print()

start = timer()
p2 = part2(packet)
end = timer()
print("Part 2:", p2)
print("Time (msec):", (end - start) * 1000)
print()
