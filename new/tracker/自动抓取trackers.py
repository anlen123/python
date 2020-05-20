import os
import time
def openBT(path):
	f = open(path)
	txt = list(filter(None, f.read().split("\n")))
	# print(len(txt))
	with open("bt_temp.txt",'a+')as f:
		for x in txt:
			f.write(x+",")
	f.close()

if __name__ == '__main__':
	url = "https://github.com/ngosang/trackerslist.git"
	if not os.path.exists("trackerslist"):
		os.system("git clone https://github.com/ngosang/trackerslist.git")
	time.sleep(1)
	# os.system("dir")
	os.chdir("trackerslist")
	# os.system("dir")
	txt_list = os.listdir()
	for file in txt_list:
		if file.endswith(".txt") and file.startswith("trackers"):
			# print(file)
			openBT(str(file))

	f = open("bt_temp.txt")
	a =list(filter(None,list(set(f.read().split(",")))))
	f.close()

	os.chdir("..")
	if os.path.exists("bt.txt"):
		os.system("del bt.txt")
	with open("bt.txt", 'a+')as f:
		f.write("bt-tracker=")
	with open("bt.txt",'a+')as f:
		for x in a:
			f.write(x+",")
	if os.path.exists("trackerslist"):
		os.system("rd /s/q trackerslist")
