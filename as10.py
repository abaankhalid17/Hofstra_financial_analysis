import re
import pdb

#Challenge 1

def extractCourse(fname):
	#1. read the entire file as one string
	f1 = open(fname, "r");
	text = f1.read();
	f1.close();

	#2. define reg pattern and ectract all tr rowa
	#r1 = re.compile("<tr.*?section_row.*?>.*?</tr>", re.MULTILINE | re.DOTALL);
	r1 = re.compile("<tr.*?section_row.*?>.*?</tr>", re.MULTILINE | re.DOTALL);
	arr = r1.findall(text);

	#3. arr2 = []
	arr2 = []

	#4. for each s in arr:
	for s in arr:
			
		#4.1 extract all data cell values
		r2 = re.compile("<td.*?>(.*?)</td>",re.MULTILINE | re.DOTALL);
		arrCells = r2.findall(s);		

		#4.2 if arrCells[3] != "&nbsp;" : inclide it in arr2
		if arrCells[3]!="&nbsp;":
			arr2.append(s);
	#5. return arr2
	return arr2

#Challenge 2

def extractMajors(arr):
	
	r1 = re.compile("<td.*?>(.*?)</td>", re.MULTILINE | re.DOTALL)

	arrRet = []
	arr3 = []
	arr4 = []
	for x in arr:
		arr2 = r1.findall(x)
		arr3.append(arr2)
		for c in arr3:
			arr4.append(c[2]);

	for v in arr4:
		if not(v in arrRet):
			arrRet.append(v);
	arrRet.pop(0);
	return arrRet;

def income(arr):
	arr3 = []
	arr4 = []
	vals = []
	fsum = 0.0
	price = 1300
	r1 = re.compile("<td.*?>(.*?)</td>", re.MULTILINE | re.DOTALL);

	for x in arr:
		arr2 = r1.findall(x)
		arr3.append(arr2)
		for c in arr3:
			arr4.append(c[6]);


	for num in arr4:
		if num != 'M':
			vals.append(float(num));

	for credit in vals:
		fsum += credit*price

	return fsum;



#Main
#pdb.set_trace();
arrCourse = extractCourse("hofstra.html")
print(arrCourse)
print("Number of courses: ", len(arrCourse))

Classes = extractMajors(arrCourse)
print(Classes);
print("Majors: ", len(Classes));

Total_Income = income(arrCourse);
print("Tuition: " , Total_Income/100)
