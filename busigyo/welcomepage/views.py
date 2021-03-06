from django.shortcuts import render
import requests
import geocoder
from .forms import TestForm,Form

# Create your views here.

#from django.http import HttpResponse

image_text = """
100 晴れ
101 晴れ時々くもり
102 晴れ一時雨
103 晴れ時々雨
104 晴れ一時雪
105 晴れ時々雪
106 晴れ一時雨か雪
107 晴れ時々雨か雪
108 晴れ一時雨か雷雨
110 晴れのち時々くもり
111 晴れのちくもり
112 晴れのち一時雨
113 晴れのち時々雨
114 晴れのち雨
115 晴れのち一時雪
116 晴れのち時々雪
117 晴れのち雪
118 晴れのち雨か雪
119 晴れのち雨か雷雨
120 晴れ朝夕一時雨
121 晴れ朝の内一時雨
122 晴れ夕方一時雨
123 晴れ山沿い雷雨
124 晴れ山沿い雪
125 晴れ午後は雷雨
126 晴れ昼頃から雨
127 晴れ夕方から雨
128 晴れ夜は雨
129 晴れ夜半から雨
130 朝の内霧のち晴れ
131 晴れ朝方霧
132 晴れ朝夕くもり
140 晴れ時々雨で雷を伴う
160 晴れ一時雪か雨
170 晴れ時々雪か雨
181 晴れのち雪か雨
200 くもり
201 くもり時々晴れ
202 くもり一時雨
203 くもり時々雨
204 くもり一時雪
205 くもり時々雪
206 くもり一時雨か雪
207 くもり時々雨か雪
208 くもり一時雨か雷雨
209 霧
210 くもりのち時々晴れ
211 くもりのち晴れ
212 くもりのち一時雨
213 くもりのち時々雨
214 くもりのち雨
215 くもりのち一時雪
216 くもりのち時々雪
217 くもりのち雪
218 くもりのち雨か雪
219 くもりのち雨か雷雨
220 くもり朝夕一時雨
221 くもり朝の内一時雨
222 くもり夕方一時雨
223 くもり日中時々晴れ
224 くもり昼頃から雨
225 くもり夕方から雨
226 くもり夜は雨
227 くもり夜半から雨
228 くもり昼頃から雪
229 くもり夕方から雪
230 くもり夜は雪
231 くもり海上海岸は霧か霧雨
240 くもり時々雨で雷を伴う
250 くもり時々雪で雷を伴う
260 くもり一時雪か雨
270 くもり時々雪か雨
281 くもりのち雪か雨
300 雨
301 雨時々晴れ
302 雨時々止む
303 雨時々雪
304 雨か雪
306 大雨
308 雨で暴風を伴う
309 雨一時雪
311 雨のち晴れ
313 雨のちくもり
314 雨のち時々雪
315 雨のち雪
316 雨か雪のち晴れ
317 雨か雪のちくもり
320 朝の内雨のち晴れ
321 朝の内雨のちくもり
322 雨朝晩一時雪
323 雨昼頃から晴れ
324 雨夕方から晴れ
325 雨夜は晴れ
326 雨夕方から雪
327 雨夜は雪
328 雨一時強く降る
329 雨一時みぞれ
340 雪か雨
350 雨で雷を伴う
361 雪か雨のち晴れ
371 雪か雨のちくもり
400 雪
401 雪時々晴れ
402 雪時々止む
403 雪時々雨
405 大雪
406 風雪強い
407 暴風雪
409 雪一時雨
411 雪のち晴れ
413 雪のちくもり
414 雪のち雨
420 朝の内雪のち晴れ
421 朝の内雪のちくもり
422 雪昼頃から雨
423 雪夕方から雨
424 雪夜半から雨
425 雪一時強く降る
426 雪のちみぞれ
427 雪一時みぞれ"
430 みぞれ
450 雪で雷を伴う
500 快晴
550 猛暑
552 猛暑時々曇り
553 猛暑時々雨
558 猛暑時々大雨・嵐
562 猛暑のち曇り
563 猛暑のち雨
568 猛暑のち大雨・嵐
572 曇り時々猛暑
573 雨時々猛暑
582 曇りのち猛暑
583 雨のち猛暑
600 うすぐもり
650 小雨
800 雷
850 大雨・嵐
851 大雨・嵐時々晴れ
852 大雨・嵐時々曇り
853 大雨・嵐時々雨
854 大雨・嵐時々雪
855 大雨・嵐時々猛暑
859 大雨・嵐一時大雪
861 大雨・嵐のち晴れ
862 大雨・嵐のち曇り
863 大雨・嵐のち雨
864 大雨・嵐のち雪
865 大雨・嵐のち猛暑
869 大雨・嵐のち大雪
871 晴れ時々大雨・嵐
872 曇り時々大雨・嵐
873 雨時々大雨・嵐
874 雪時々大雨・嵐
881 晴れのち大雨・嵐
882 曇りのち大雨・嵐
883 雨のち大雨・嵐
884 雪のち大雨・嵐
950 大雪
951 大雪時々晴れ
952 大雪時々曇
953 大雪一時雨
954 大雪時々雪
958 大雪一時大雨
961 大雪のち晴れ
962 大雪のち曇
963 大雪のち雨
964 大雪のち雪
968 大雪のち大雨・嵐
971 晴れ一時大雪
972 曇一時大雪
973 雨一時大雪
974 雪一時大雪
981 晴れのち大雪
982 曇のち大雪
983 雨のち大雪
984 雪のち大雪
999 No Data
"""


#def index(request):
#    li=[]

#    for i in image_text.split():
#        if i.isdigit():
#            li+=[i]
#    my_dict = {
#        'image_head':"static/images/",
#        #'images_titles': li,
#        'image_num':'100',
#        'image_tail':".png",
#        'form': TestForm(),
#        'insert_forms': '',
#    }
#    if (request.method == 'POST'):
#        #my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '\n整数型:' + request.POST['num']
#        #my_dict['form'] = TestForm(request.POST)
#        my_dict['image_num'] = request.POST['num'];
#    return render(request, 'index.html',my_dict)

#def index2(request):
#    return HttpRespnse("MASUNO SLEEP MODE")

API_Key = 'ciCs66mDVE6OUlonzEs6R95ouMHi5sV7jiAPV0Hf'
HEADERS = {'X-API-Key': API_Key}
URL = 'https://wxtech.weathernews.com/api/v1/ss1wx'

def forecast(request):
    wx_list=[]
    feeltmp_list=[]
    feelidx_list=[]
    location = '八街市'

    # ここのパラメーター変えたい
    query = {
        'lat': 35.6658607,
        'lon': 140.3178646,
    }
    if (request.method == 'POST'):
        #my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '\n整数型:' + request.POST['num']
        #my_dict['form'] = TestForm(request.POST)
        #print(request.POST)
        location = request.POST['loc']
        #現在地を取得
        latlon = geocoder.osm(location, timeout=5.0).latlng
        query['lat'] = latlon[0]
        query['lon'] = latlon[1]
        #query['lat'] = request.POST['lat']
        #query['lon'] = request.POST['lon']

    r = requests.get(URL, params=query, headers=HEADERS)
    data=r.json()

    # print("response", data)
    # print()
    # print(data["requestId"])
    srf=data["wxdata"][0]["srf"]
    for i in srf[0:12]:
        wx_list+=[i['wx']]
        feeltmp_list+=[i['feeltmp']]
        feelidx_list+=[i['feelidx']]

    max_feelidx = max(feelidx_list)
    min_feelidx = min(feelidx_list)
    tops_table = {
        'A': '熱中症に注意した服装を心がけましょう。',
        'B': '薄手布地の長袖がお勧めです。',
        'C': '薄い布地では少し肌寒いです。',
        'D': '肌寒いので上着は忘れずに。',
        'E': '厚手の上着で体温を調節しましょう。',
        'F': '最大限の防寒を忘れずに。',
    }

    bottoms_table = {
        'A': '涼しい布地がお勧めです。',
        'B': '薄手の長ズボンがお勧めです。',
        'C': '長ズボンがお勧めです。',
        'D': '厚手の長ズボンがお勧めです。',
        'E': '厚手の長ズボンがお勧めです。',
        'F': 'できるだけ厚手のものを選びましょう。',
    }

    shoes_table = {
        'A': 'サンダルまたはスニーカーがお勧めです。',
        'B': 'スニーカーがお勧めです。',
        'C': 'スニーカーがお勧めです。',
        'D': '厚めの靴下を着用しましょう。',
        'E': '厚手の長ズボンがお勧めです。',
        'F': '厚手の靴下を着用しましょう。',
    }
    my_dict = {
        'image_head':"static/images/",
        'today_weather': data["wxdata"][0]["mrf"][0]['wx'],
        'images_titles': wx_list,
        'feeltmp_list': feeltmp_list,
        'feelidx_list': feelidx_list,
        'zipped_data': zip(wx_list, feeltmp_list, feelidx_list),
        'max_feeltmp': max(feeltmp_list),
        'min_feeltmp': min(feeltmp_list),
        'max_tmp': data["wxdata"][0]["mrf"][0]['maxtemp'],
        'min_tmp': data["wxdata"][0]["mrf"][0]['mintemp'],
        'pop_message': '',
        'tops_message': '',
        'bottoms_message': '',
        'shoes_message': '',
        'temp_diff_message': '',
        'location': location,
        'image_num':'100',
        'image_tail':".png",
        'form': Form(),
        'insert_forms': '',
        'lat': query['lat'],
        'lon': query['lon'],
    }

    if (max_feelidx >= 6):
        my_dict['tops_message'] = tops_table['A']
        my_dict['bottoms_message'] = bottoms_table['A']
        my_dict['shoes_message'] = shoes_table['A']
    elif (max_feelidx == 5):
        my_dict['tops_message'] = tops_table['B']
        my_dict['bottoms_message'] = bottoms_table['B']
        my_dict['shoes_message'] = shoes_table['B']
    elif (max_feelidx == 4):
        my_dict['tops_message'] = tops_table['C']
        my_dict['bottoms_message'] = bottoms_table['C']
        my_dict['shoes_message'] = shoes_table['C']
    elif (max_feelidx == 3):
        my_dict['tops_message'] = tops_table['D']
        my_dict['bottoms_message'] = bottoms_table['D']
        my_dict['shoes_message'] = shoes_table['D']
    elif (max_feelidx == 2):
        my_dict['tops_message'] = tops_table['E']
        my_dict['bottoms_message'] = bottoms_table['E']
        my_dict['shoes_message'] = shoes_table['E']
    else:
        my_dict['tops_message'] = tops_table['F']
        my_dict['bottoms_message'] = bottoms_table['F']
        my_dict['shoes_message'] = shoes_table['F']

    if ((max_feelidx >= 6) & (min_feelidx <= 4)):
        my_dict['temp_diff_message'] = '昼夜の温度差が激しいので上着を用意しましょう。'
    elif ((max_feelidx == 5) & (min_feelidx <= 3)):
        my_dict['temp_diff_message'] = '昼夜の温度差が激しいので上着を用意しましょう。'
    elif ((max_feelidx == 4) & (min_feelidx <= 2)):
        my_dict['temp_diff_message'] = '朝晩は冷え込むので上着は忘れずに持参しましょう。'

    if (data["wxdata"][0]["mrf"][0]['pop'] > 50):
        my_dict['pop_message'] = '傘を持っていきましょう。'

    return render(request, 'forcast.html',my_dict)

#forecast(1)

#geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
#data = requests.get(geo_request_url).json()
#print(data['latitude'])
#print(data['longitude'])
#print(data)

#place = '八街市'
#ret = geocoder.osm(place, timeout=5.0).latlng
#print(place, ret[0])
