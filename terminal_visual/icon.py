import os,sys

def hSeperate(Len):
	return "-"*Len

def Stringer(lines,FixLen):	
	str = ""
	for line in lines:
		if len(line) < 35:
			str += line + " "*(35-len(line)) + "\n"
		else:
			str += line + "\n"
	return str

def Bitcoin():
	lines = []
	lines.append("BTC")
	lines.append("---- __▉_▊_    ")
	lines.append("    |▉▉▉▉▉▉\   ")
	lines.append("      |▉|_)▉|  ")
	lines.append("      |▉▉▉▉▉▙. ")
	lines.append("     _|▉|__)▉| ")
	lines.append("    |▉▉▉▉▉▉▉/  ")
	lines.append("      ▉ ▉      ")
	lines.append("               ")
	return lines

def Ether():
	lines = []
	lines.append("ETH")
	lines.append("---     /\     ")
	lines.append("       /  \    ")
	lines.append("      /    \   ")
	lines.append("     /      \  ")
	lines.append("     \"::::::\"  ")
	lines.append("      \ \"\" /   ")
	lines.append("       \  /    ")
	lines.append("        \/     ")
	return lines

def Lite():
	lines = []
	lines.append("LTC")
	lines.append("---     __    ")
	lines.append("       / /    ")
	lines.append("      /▰/▰▰   ")
	lines.append("     /▰/      ")
	lines.append("  ▰▰/▰/       ")
	lines.append("   / /______  ")
	lines.append("   \________| ")
	lines.append("              ")
	return lines


