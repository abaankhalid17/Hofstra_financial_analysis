# Hofstra Financial Analysis

![](https://github.com/abaankhalid17/Hofstra_financial_analysis/blob/main/hofstra%20banner.png)

## Overview
This project involves a financail analysis of Hofstra University's Fall 2018 semester. The goal is to extract valuable insights and find out how much Hofstra University makes off tuition in the Fall 2018 semester. The following README provides a detailed account of the project's objectives, solutions, findings, and conclusions.

## 1. Extract Course Sections.

- First I defined a function named “extractCourse”, which returns an array of strings. Each string contained the entire record for one course.

```python3
def extractCourse(fname):
	#1. read the entire file as one string
	f1 = open(fname, "r");
	text = f1.read();
	f1.close();
```

## 2. One Record of a Course Selection

- Each record starts with a <tr> tag, which contains “section_row” and it ends with a </tr> tag. A regular expression can easily capture the pattern.

- Once I retrieved the matches of the above search pattern, I still needed to do an additional round of filtering, because some records are fake records. They were actually the final exam date entries. I inspected the content of the 3rd <td> tag of each record. If it was not &nbsp; it was a real course record; otherwise it was a final exam date entry. For accomplishing this check, I used another regular expression pattern to extract an array of <td> tag contents, and checked the 3rd element of the array.

## 3. Extracting number of courses using special form of compile function

```python3
r1 = re.compile("<tr.*?section_row.*?>.*?</tr>", re.MULTILINE | re.DOTALL);
r1 = re.compile("<tr.*?section_row.*?>.*?</tr>", re.MULTILINE | re.DOTALL);
	arr = r1.findall(text);

arr2 = []
	arr2 = []
```

## 4. Extracting all data from cell values

```
for each s in arr:
	for s in arr:
			
		#4.1 extract all data cell values
		r2 = re.compile("<td.*?>(.*?)</td>",re.MULTILINE | re.DOTALL);
		arrCells = r2.findall(s);		

		#4.2 if arrCells[3] != "&nbsp;" : inclide it in arr2
		if arrCells[3]!="&nbsp;":
			arr2.append(s);
```

## 5. Retruning Array 2

```
return arr2
	return arr2
```

## 6. Extracting Majors

- To figure out how many majors are offered by Hofstra I looked at the major code (e.g., “ACCT” and “CSC”) in the course catalog. Since extractCourse() returns an array of strings, I defined an additonal function named “extractMajors(arr)”, which given the output of extractCourse(), returns an array of strings and each element is a distinct major code.

```
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
```

## 7. Extracting elements from Array

- I defined a regular expression to capture the patterns of <td>…</td> tags and then the major code is the third element.

## 8. Tution Income

- After finding out that the per credit cost for the Fall 2018 semester was $1380, I applied that to find the tuition income for Fall 2018.

```
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

```
## Findings & Conclusion
- Collected data from Hofstra University’s public catalog, on class size and tuition rate, to calculate the total tuition income of the university
- Utilized Python to create functions such as “extractCourse” and “extractMajor” to extract the 3874 courses and 130 majors
- Utilized regular expressions HTML tags like <t>, </tr>, $nbsp, and <td> to help filter through the fake records or final exam dates
- By using Python’s debugger to solve the logical errors in the code, created another function, “income”, taking the data from Hofstra’s public course catalog, set the price to the $1380 cost per credit and solved to find the total tuition for the semester to be $254,144,044





 

