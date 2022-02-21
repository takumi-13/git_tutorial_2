#%%
from bs4.element import NavigableString
import requests
from bs4 import BeautifulSoup
from requests.api import get

soup = BeautifulSoup(open('target.html'),'html.parser')

def getClassNames (contents):
  className = contents.attrs['class']
  return className

def getTagName (contents):
  tagName = contents.name
  return tagName

def makeCode (res,tagName,className):
  classNameRes = ""
  for c in className:
    classNameRes += c + ", "
  result = res + tagName + ", " + classNameRes
  return result

def getContents (content) :
  if not(type(content) is NavigableString):
    tagName= getTagName(content)
    className = getClassNames(content)
    return tagName,className
  #ありえない挙動
  else:
    return 'None', 'None'

def appendList (content,tagList,classList):
  tagName,className, = getContents(content)
  tagList.append(tagName)
  classList.append(className)

resultTagList = []
resultClassList = []
resultIdList = []

links = soup.find_all('div', class_='box-styleguide')

for link in links:
  idList = []
  tagList = []
  classList = []
  contents = link.contents[5]
  getTagCount1 = 0
  getTagCount2 = 0
  getTagCount3 = 0
  getTagCount4 = 0
  getTagCount5 = 0
  for c1 in contents.children:
    if not(type(c1) is NavigableString):
      if getTagCount1 == 0:
        appendList(c1,tagList,classList)
        getTagCount1 += 1
        for c2 in c1.children:
          if not (type(c2) is NavigableString):
            if getTagCount2 == 0:
              appendList(c2,tagList,classList)
              getTagCount2 += 1
              for c3 in c2.children:
                if not (type(c3) is NavigableString):
                  if getTagCount3 == 0:
                    appendList(c3,tagList,classList)
                    getTagCount3 += 1
                    for c4 in c3.children:
                      if not (type(c4) is NavigableString):
                        if getTagCount4 == 0:
                          appendList(c4,tagList,classList)
                          getTagCount4 += 1
                          for c5 in c4.children:
                            if not (type(c5) is NavigableString):
                              if getTagCount5 == 0:
                                appendList(c5,tagList,classList)
                                getTagCount5 += 1
  resultIdList.append (link['id'])
  resultTagList.append (tagList)
  resultClassList.append (classList)
print (resultIdList)
print (resultTagList)
print (resultClassList)

# %%
startString = "map.put("
pattern  = ', patternXX(root, '
# 答えは：map.out(m-05-a-v2, patternXX (root, p, txt-read, p, txt-read__inner))みたいな形にしたい
tmp = []
for res in zip (resultIdList,resultTagList,resultClassList):
  tmp.append(res)
result = []
for elem in tmp:
  res = startString + elem[0] + pattern
  for item in zip (elem[1],elem[2]):
    res = res + item[0] + ", " +  ", ".join(item[1]) + ", "
  res = res[:-2]
  res += ")"
  result.append (res)
print (result)

# %%
