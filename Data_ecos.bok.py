import requests
import xml.etree.ElementTree as ET
import xml.dom.minidom

# 발급받은 인증키
auth_key = 'N675Z5KRA3UW6T2JU6F6'

# API 호출을 위한 기본 URL
url = "http://ecos.bok.or.kr/api/StatisticSearch/sample/json/kr/1/10/010Y002/MM/201101/201106/AAAA11/"

# API 요청 보내기
response = requests.get(url)

# 응답 데이터 확인
data = response.json()
print(data)
#rdata = data['StatisticSearch']['row']

# 받아온 데이터를 데이터프레임으로 변환
import pandas as pd
#df = pd.DataFrame(rdata)
#df.set_index("TIME", inplace=True)


'''
# http 요청이 성공했을 때 API 리턴값 가져오기
if response.status_code == 200:
    try:
        contents = response.text
        ecosRoot = ET.fromstring(contents)

        # 호출결과에 오류 있는지 확인
        if ecosRoot[0].text[4] in ("INFO","ERRO"):
            print(ecosRoot[0].text + " : " + ecosRoot[1].text)
        else:
            dom = xml.dom.minidom.parseString((contents))
            pretty_xml_as_string = dom.toprettyxml(indent="  ")
            print(pretty_xml_as_string)
    except Exception as e:
        print(str(e))
'''


