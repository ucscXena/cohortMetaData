import string, json, sys, re
import itertools

def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

# less chopping
def decomposeEntry(A):
	return map(lambda x: string.strip(x),
		flatten(map(lambda x: string.split(x, ' - '),
			re.split('\(|\)|\/|\_|\&|\,|\;|\:', A))))

# more chopping : chop including space
def chopUpWords(A):
	return re.split('\(|\)|\/|\_|\&|\,|\;|\:|\ ', A)

def processTumorType(file):
	objDic = {}
	fin = open(file,'r')
	line = fin.readline()
	headers = string.split(line[:-1],'\t')
	for line in fin.readlines():
		obj={}
		data = string.split(line[:-1],'\t')
		for i in range (0, min(len(headers), len(data))):
			if data[i] != "" and headers[i] != "metacolor":
				if headers[i] == "metanci" or headers[i] == "metauml":
					obj[headers[i]] = data[i]
				else:
					obj[headers[i]]  = map(lambda x: string.strip(x), decomposeEntry(data[i]))
		if obj.has_key("metanci"):
			objDic[obj["metanci"]] = obj
	fin.close()
	return objDic

def buildNewJson (originalJson, oncoTreeDic):
	tagDic ={}
	for cohort in originalJson.keys():
		if cohort == "_comment":
			continue
		tagDic[cohort] =[]
		
		# cohort name tag
		tagDic[cohort].extend(chopUpWords(cohort))

		obj = originalJson[cohort]
		# existing tag
		if obj.has_key("tag"):
			tagDic[cohort].extend(obj["tag"])

		# existing raw material
		if obj.has_key("raw"):
			newList = flatten(map(lambda x: decomposeEntry(x), obj["raw"]))
			tagDic[cohort].extend(newList)

		#info from oncotree tumorTypeF 
		if obj.has_key("metanci"):
			for metanci in obj["metanci"]:
				tagDic[cohort].extend(flatten(oncoTreeDic[metanci].values()))

		#"A B" add "A" "B"
		newList = tagDic[cohort][:]
		map(lambda x: newList.extend(re.split(' ', x)), tagDic[cohort])
		
		#"A-B" add "AB"
		tagDic[cohort] = newList
		newList = tagDic[cohort][:]
		map(lambda x: newList.append(string.replace(x,'-','')), tagDic[cohort])
		tagDic[cohort] = newList

		#existing code
		if obj.has_key("code"):
			tagDic[cohort].extend(obj["code"])

		#clean up
		tagDic[cohort] = list(set(i.title() for i in tagDic[cohort]))
		tagDic[cohort] = filter(None, tagDic[cohort])
		tagDic[cohort] = filter(lambda x: x not in ["And", "But", "By", "An", "The", "A", '-', ':'], tagDic[cohort])
		tagDic[cohort].sort()

	return tagDic

def buildNewJsonWithCompositeCohort(originalJson, inputJ):
	for cohort in originalJson.keys():
		if cohort == "_comment":
			continue

		originalObj = originalJson[cohort]

		if originalObj.has_key("composite_cohots"):
			tag = inputJ[cohort]

			for sub_cohort in originalObj["composite_cohots"]:
				tag.extend(inputJ[sub_cohort])

			#clean up
			tag = list(set(i.title() for i in tag))
			tag.sort()
			inputJ[cohort] = tag
	return inputJ


if len(sys.argv[:])!=4:
	print "python script.py onco_tree_tumortype.txt json_input output"
	sys.exit()

tumorTypeF = sys.argv[1]
oncoTreeDic = processTumorType(tumorTypeF)

jsonInput = open(sys.argv[2],'r')
J = json.load(jsonInput)

newJ = buildNewJson(J, oncoTreeDic)

newJ = buildNewJsonWithCompositeCohort(J, newJ)

foutput = open(sys.argv[3],'w')
json.dump(newJ, foutput, indent=2)
foutput.close()









