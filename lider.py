import requests
import time
import json
import time
import datetime  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

start_time = time.time() 
#Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json' #Cambiar check
SPREADSHEET_ID = '1LnQY2tABOaIN86_q80p24RNGFR3h_eTI9JVOF6HfeB4' #Cambiar check
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# URL base y parámetros de la solicitud
base_url = "https://apps.lider.cl/supermercado/bff/products/"
query_params = {"appId": "BuySmart", "ts": "1709842514374"}

# Lista de SKUs a probar
skus1 ={ "7802215108174": "11242"}
skus = {
    "7802215108174": "11242",
    "7702367463421": "299055",
    "7802410001621": "699590",
    "4000417018007": "331002",
    "7801610001523": "278598",
    "4000417700001": "331002",
    "7801610350850": "3895",
    "7801620014681": "279011",
    "7801620006877": "849874",
    "7802215501838": "2911",
    "7803111001705": "672798",
    "7896019208468": "586517",
    "8801055709212": "999654",
    "8801055709274": "1005973",
    "7613031891344": "299973",
    "7809583500319": "59",
    "7802410003182": "909893",
    "7802710835155": "7265",
    "7802710835216": "4609",
    "7802710832116": "4591",
    "7702010130243": "1026433",
    "7702010130250": "5991",
    "7802420007934": "5187",
    "7802420007927": "279037",
    "7802900130114": "809126",
    "7802900001414": "916656",
    "7613287593283": "592302",
    "7790290001193": "479025",
    "7804615340567": "4465964",
    "7802107000869": "276334",
    "7802107000999": "1400350",
    "7801365000284": "3763",
    "7804454005788": "322173",
    "7802575034014": "275472",
    "7613032596668": "874928",
    "7891000248768": "972747",
    "7805000141271": "1889",
    "7802230076298": "283089",
    "7802900002855": "1393737",
    "23049": "325468",
    "7804300143657": "937099",
    "7804945002197": "281677",
    "7802920777283": "2061",
    "7804300143671": "266954",
    "7891150067707": "1042902",
    "7802710350504": "4607",
    "7500435160544": "769822",
    "7802000017186": "269594",
    "7802000015632": "891614",
    "7802000015649": "891616",
    "7801305004167": "590058",
    "7896004004549": "659387",
    "7613035652101": "821792",
    "7808704700850": "849924",
    "7808704700966": "965226",
    "7802420007958": "145680",
    "22010": "264220",
    "70847009511": "539998",
    "7802215511011": "3015",
    "7801620370107": "5925",
    "8410376017113": "744951",
    "7802230086952": "2969",
    "7613034891730": "686589",
    "7802215514326": "2927",
    "7802225682121": "386938",
    "7804649810074": "1100411",
    "7802940001795": "1020246",
    "8001665700047": "739669",
    "8005121216011": "336878",
    "7802940730701": "603655",
    "7809611708410": "689308",
    "7809611700513": "742351",
    "7802626161010": "279311",
    "7802626100026": "743686",
    "7802626100040": "279305",
    "7802626100057": "279319",
    "7802626001552": "1329631",
    "7790272001005": "281689",
    "7802626001477": "1175405",
    "7802820441802": "279551",
    "7797453001519": "882010",
    "7802615006551": "2405",
    "7802626001576": "1289147",
    "7730219021338": "1104866",
    "7804920007605": "740876",
    "7804920350855": "269508",
    "7702367003900": "861190",
    "7801970001478": "1136663",
    "7702367003917": "1104836",
    "22085": "758483",
    "7805000322014": "1342363",
    "7802000013621": "654076",
    "7802000013607": "654072",
    "7801230004409": "287351",
    "7802920777542": "5101",
    "7801610001622": "3935",
    "7802920007403": "859414",
    "7801610350409": "3879",
    "7801620006891": "847350",
    "7803111001682": "672800",
    "7801315000326": "4461679",
    "7801970001003": "118482",
    "7809611711120": "684328",
    "7802920202105": "2073",
    "7804000002490": "1026419",
    "7802920203300": "2071",
    "7802920203409": "2081",
    "7804634400501": "1100409",
    "7805000312329": "5671",
    "7802420124525": "1207235",
    "21000026326": "280661",
    "7803908006197": "1062877",
    "7613287593481": "1217892",
    "7809611700667": "2259",
    "80177173": "279629",
    "7802100000330": "937361",
    "7802100001788": "704136",
    "7802000012587": "903781",
    "7801300301049": "279683",
    "7809611701268": "312509",
    "7803480001313": "1095991",
    "7803480001269": "1047526",
    "7802230070227": "283107",
    "7803473212238": "290071",
    "7803480000309": "266522",
    "7806500174202": "1278581",
    "7802230070029": "106",
    "7801300000096": "355279",
    "7801300000072": "268456",
    "23028": "323766",
    "7802920000435": "2063",
    "7500435182225": "911556",
    "99176480310": "11075",
    "7891024005064": "895179",
    "7801300000065": "331446",
    "7801970026433": "585517",
    "7808704700843": "849922",
    "7808704700973": "965228",
    "7809611707468": "344005",
    "7806300010021": "290941",
    "7802175455493": "514756",
    "7802175455912": "589822",
    "7802225640770": "541556",
    "7802215502262": "2959",
    "7802926001085": "550065",
    "7802926000965": "1131058",
    "7802926001580": "1081606",
    "7802926000033": "293069",
    "7802926000071": "293099",
    "7802926000132": "290359",
    "7802926000101": "290345",
    "7802926001931": "729675",
    "7802926000149": "293061",
    "7802926000750": "293037",
    "7802926000170": "290391",
    "7802926001849": "1390363",
    "79344007273": "117144",
    "79344007204": "336456",
    "79344007235": "125112",
    "79344007228": "915393",
    "451": "438058",
    "7802215508547": "5385",
    "7802215505027": "2929",
    "7802900003265": "1402209",
    "7802225682107": "295027",
    "1361": "806638",
    "825": "997678",
    "7801970000990": "585513",
    "7801970004783": "6825",
    "7801930019055": "280815",
    "7809611719171": "1166015",
    "54": "701367",
    "7797453000802": "769451",
    "7797453000475": "8081",
    "7802615005615": "297219",
    "70177078966": "843459",
    "70177078904": "823249",
    "7806500406747": "309243",
    "7802615005103": "3033",
    "7806500406709": "4081",
    "7802615005202": "3035",
    "7801970001409": "1094357",
    "7802095180123": "880285",
    "7805040004451": "917581",
    "7802615005400": "296263",
    "7730219021390": "1104864",
    "7804300121396": "286007",
    "7804320750552": "1026903",
    "7801235131117": "2669",
    "7804320758626": "4443393",
    "8410113002150": "1154302",
    "7804626930054": "1016578",
    "7804669210007": "4433761",
    "7797453972345": "1005610",
    "7797453972260": "1005606",
    "7797453972291": "1005612",
    "7797453972390": "1005608",
    "7802920007120": "3107",
    "80432400432": "258950",
    "5000267014005": "1401",
    "7790272007366": "1034873",
    "8715200813061": "368961",
    "7802920000084": "5103",
    "7802920000091": "5105",
    "7802410001379": "296941",
    "7802575533616": "1059092",
    "4067700018243": "860270",
    "7803908006821": "1270854",
    "7801610333129": "432282",
    "23042": "476644",
    "7801610778548": "1283419",
    "7802420127113": "5785",
    "7802920001326": "298129",
    "21000026968": "5915",
    "7801620853396": "11295",
    "7501058743145": "472362",
    "7501058743121": "472362",
    "7801875069368": "5641",
    "7802130002274": "993393",
    "4009900412087": "594745",
    "7803403003257": "266222",
    "7802200230293": "283883",
    "7802420002359": "815757",
    "8410036009090": "18551",
    "7891024078174": "1008287",
    "4053400279398": "740892",
    "7806500512769": "917082",
    "7801305004099": "531717",
    "7802225582476": "886507",
    "7702174084062": "1355544",
    "7622201797560": "1135221",
    "99": "937343",
    "7802900001339": "937345",
    "7802930004720": "983652",
    "4005808890590": "299051",
    "37000401520": "596916",
    "7801300000157": "279719",
    "7804320449098": "752026",
    "7804454004873": "755832",
    "7613030612339": "2933",
    "7806500962809": "359741",
    "7802500008042": "2689",
    "7809558102487": "533193",
    "7804300010614": "5599",
    "7804300122959": "285215",
    "7622201693138": "567236",
    "7898279792077": "1087492",
    "7804320746104": "954921",
    "5000299628034": "1081266",
    "7801235001991": "1203135",
    "7804673610121": "4514248",
    "70177197360": "838034",
    "7805000315122": "937829",
    "7801970001485": "1136665",
    "7802800579518": "916222",
    "8445290262790": "1381282",
    "7804619570038": "295029",
    "8006550342067": "1384498",
    "7801610002650": "5761",
    "7802900001421": "1113353",
    "7801620001223": "4027",
    "7804086000311": "963773",
    "7808743600500": "278558",
    "7801960000290": "737434",
    "7805040001832": "4513724",
    "7801620016036": "806218",
    "7801970001034": "571223",
    "7801620001643": "4023",
    "7861002900117": "295033",
    "7613287581099": "300833",
    "7802410305033": "751374",
    "7802920221328": "3123",
    "650240050114": "1163170",
    "7802225280655": "280523",
    "8445290091833": "4619",
    "7802100003768": "4518168",
    "7803468001427": "897120",
    "7803468000123": "290767",
    "7803468001748": "1004650",
    "7803468002257": "291935",
    "7802930003679": "520558",
    "7801970000143": "7149",
    "7802410112136": "751372",
    "7791290792487": "656712",
    "76150601244": "2549",
    "76150601336": "2551",
    "7802410101376": "751360",
    "7802926001917": "729677",
    "7802926001900": "729681",
    "7802930002498": "318849",
    "7802930002504": "700010",
    "7802920000749": "4223",
    "7803520140026": "285641",
    "7613036566377": "320121",
    "78021624": "749008",
    "7803600002367": "1284958",
    "7802180068169": "10666",
    "78895126396": "450501",
    "650240011832": "819273",
    "7802575004437": "2713",
    "7613030518426": "499051",
    "7613036310925": "898258",
    "7802930003907": "704675",
    "7802225000314": "997805",
    "70177177430": "920987",
    "7804630010582": "882750",
    "7898591453274": "901772",
    "7804330141111": "4527",
    "7806810000574": "7325",
    "7808729601200": "576334",
    "7804320256900": "5935",
    "7804454000882": "322173",
    "7804330006946": "821918",
    "7808704701031": "1016582",
    "7802900028473": "5041",
    "7802920007137": "946429",
    "7802910083509": "291629",
    "7804600778924": "311599",
    "7804600770171": "311439",
    "7805040313027": "297373",
    "7804320365848": "1441",
    "7808765747689": "4481661",
    "7801930000602": "3877",
    "7802900003524": "4427373",
    "7802175453222": "1349",
    "7802900002107": "996441",
    "7801300000034": "279695",
    "7802900002138": "996133",
    "7802920003429": "4516889",
    "7802095000209": "295923",
    "7802920801681": "5273",
    "7802900001360": "277418",
    "7808760900478": "269930",
    "7802950006612": "3455",
    "7804335171113": "4519",
    "7804320272252": "311471",
    "7613037071368": "283671",
    "7707211631469": "335288",
    "7808704700164": "494682",
    "7808704700003": "1487",
    "715126000116": "5511",
    "7804315001065": "1495",
    "7803110102212": "314427",
    "7804300123925": "1461",
    "7804340909053": "5595",
    "82184000335": "602725",
    "781159838477": "1290033",
    "7613033081477": "880925",
    "7802930004843": "1018797",
    "7802920005294": "760666",
    "7805000321581": "1175931",
    "7613030049883": "3127",
    "7805000321567": "1175927",
    "7804918401651": "425174",
    "7802575353047": "7923",
    "7802351451400": "279249",
    "7802810002099": "2321",
    "7802640720538": "5675",
    "7802575341143": "295101",
    "7802575341136": "295139",
    "7802950012316": "5525",
    "7806500225812": "113664",
    "7801970026082": "289503",
    "7801875047137": "307191",
    "7801505231950": "2439",
    "7802575004635": "2717",
    "7801610000571": "427110",
    "8445290118288": "4460120",
    "8445290841575": "4501801",
    "7805040004765": "1161228",
    "7896005806760": "964896",
    "7802820650013": "965184",
    "8000070036116": "904465",
    "7801875047113": "2513",
    "7801610000601": "431535",
    "7801875052056": "2505",
    "7806500225522": "309127",
    "7801610001295": "299369",
    "7801875069177": "298345",
    "7801620852955": "4385",
    "7802900003319": "4427379",
    "7801620017552": "3943",
    "9002490214852": "11417",
    "7802107000913": "1192692",
    "7802107000074": "276334",
    "7801620011604": "4405",
    "7802100004024": "1060841",
    "7613039352151": "1045810",
    "7801610001196": "3963",
    "9002490221010": "586993",
    "9002490100070": "4247",
    "7801620006341": "802392",
    "7613036188302": "886523",
    "7802215102912": "350057",
    "40000514251": "838032",
    "7801620000738": "4401",
    "7801610002261": "4107",
    "7801620011611": "4403",
    "4008400221021": "1003489",
    "7802215121319": "500649",
    "22110079806": "739306",
    "7802100003249": "997706",
    "7802200134010": "298495",
    "7801300001024": "588785",
    "7801300000218": "550071",
    "7801930015538": "907956",
    "7802100004000": "1060839",
    "7802215121258": "11240",
    "7613034439277": "585334",
    "7802900105013": "289261",
    "7898024396994": "933385",
    "7898024395072": "144804",
    "7802215104855": "659758",
    "7614500010013": "283955",
    "7802215101625": "818319",
    "7802215505058": "716785",
    "7801300305047": "279717",
    "7802920776163": "289497",
    "7802900401016": "2105",
    "7802920221458": "3115",
    "7802920007397": "859410",
    "7802920007182": "3069",
    "5000267116419": "623999",
    "7802900001209": "937349",
    "7802900001926": "916654",
    "7802080000122": "265546",
    "7802920006741": "806638",
    "7802920004112": "438054",
    "7802000015182": "437287",
    "7802000017629": "891612",
    "7804454005771": "1015651",
    "8410113005298": "289419",
    "7804330006922": "821916",
    "7802940002006": "603657",
    "7802920242514": "2153",
    "7312040017010": "5507",
    "7804300000363": "269644",
    "7891136057029": "583202",
    "5000329002254": "1359",
    "7802110001952": "468481",
    "7802110001402": "289073",
    "7804300129491": "268516",
    "7802080000146": "296115",
    "7804454005764": "1015649",
    "7804300121440": "1481",
    "7804454001384": "719569",
    "7804454001544": "5515",
    "8000368244605": "752016",
    "7802950006766": "3435",
    "7804330121113": "4523",
    "7803960000553": "721643",
    "7804300131715": "266954",
    "8000368219801": "574090",
    "7802410141389": "751342",
    "7804300010508": "268642",
    "7802940002013": "603655",
    "7804300121457": "1479",
    "7802351001810": "1039573",
    "70177197230": "586513",
    "7802410350804": "3397",
    "7805300053908": "1139085",
    "7790520012524": "718211",
    "70177197308": "288005",
    "7803300300640": "292155",
    "7801930009308": "748898",
    "7801930001586": "4490087",
    "7804671930337": "1409696",
    "7802410350651": "268874",
    "7802832000264": "1340013",
    "7802410002253": "774173",
    "7791293046242": "869823",
    "650240035401": "950625",
    "7804910019434": "300703",
    "4002103248293": "4513579",
    "7801930008219": "431573",
    "7802215107139": "4468461",
    "7809611718723": "1092538",
    "7801220004891": "1039132",
    "7804000002575": "1140434",
    "7804627650227": "562992",
    "7804627650258": "348055",
    "7803520002355": "667875",
    "7802920003313": "618077",
    "7802920010632": "4501423",
    "7802832000240": "1340011",
    "7802920802282": "4427370",
    "79400301161": "634249",
    "7801305003191": "275754",
    "7802955010850": "958383",
    "7802920008004": "906650",
    "7802960808121": "528998",
    "7804627330686": "575444",
    "7804320753607": "292657",
    "7802900003517": "4427370",
    "7802960626541": "987767",
    "7804320933153": "292597",
    "7804300157647": "4511160"
}

# Puedes añadir más SKUs según sea necesario

# Encabezados de la solicitud
headers = {
    "cookie": "TSe3289311027=08d7615097ab200063f8cb10900827109c0379f88541e53e039c5aebc6390c316fb63f3a147b512a087a34f34b11300041169028f334aa7e3a402f0cff3633a733f5c71f070aef6a26fd1d531c4e2eb3dfc8d76794e9a19f321b74dc8f81e6ba; TS01cc7ea9=01680904b297b641a3ffe2c67006c76253a951620b7038f46c192bb50c0e5d613f146bd0c83dd5d878d76647620dd1b7d49eb3ce4e; TS017e8d10=01680904b297b641a3ffe2c67006c76253a951620b7038f46c192bb50c0e5d613f146bd0c83dd5d878d76647620dd1b7d49eb3ce4e",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,es-CL;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "X-FlowId": "40641ac1-08fe-49b5-b5ca-6ecd01b1a28e",
    "tenant": "supermercado",
    "X-SessionId": "f5bb090b-2a62-4267-96f4-4c5f1dd7c402",
    "x-channel": "SOD",
    "Origin": "https://www.lider.cl",
    "Connection": "keep-alive",
    "Referer": "https://www.lider.cl/",
    "Cookie": "_ga_835TB8N4KP=GS1.1.1709842463.85.1.1709842514.9.0.0; _ga=GA1.2.2023076641.1693593270; _ga_PNF51KE2NM=GS1.1.1709842463.83.1.1709842514.9.0.0; _ga_LT7B42QQTE=GS1.1.1709842463.85.1.1709842514.0.0.0; _ga_9FZFY51HX9=GS1.1.1708912082.77.0.1708912082.0.0.0; _ga_S5V4J9JZ4W=GS1.1.1709842463.83.1.1709842514.9.0.0; rxVisitor=1693593270678GE63D6AHMVKH4MU2S3FMTIC9204610JU; cto_bundle=RzpvmV81RVNmViUyRkJEODlIbThCbWFJcGl3cW1PdW9Ea2RzTnkzd0pZM1dwckYycW9sJTJGTGN5YlFsemElMkZTZVVUR2xid05td2NQUnVabEdmWVdoYmYzdyUyQkF4Ykxsb3RMczJhaU8lMkIlMkJPOHVneGlEeDN6SnZzbGFFJTJGaUVFMEZiTDh4M0pMYnVvcDEwVlZ4YXFGMnJucWwyZTJLRzU4USUzRCUzRA; fs_uid=#16PCMB#090573e9-099c-4f70-8f4e-b64c3e0c16b5:e5e2682c-160e-45aa-b57c-8d16b7add522:1709842466678::1#/1725129277; _fbp=fb.1.1693593280351.78350637; _tt_enable_cookie=1; _ttp=dQS73-PlaWhiEHJCMneOm0rD-qV; _ga_F0EXSQRJ7V=GS1.2.1707482954.57.0.1707482954.60.0.0; _ga_8MK6W43P8R=GS1.2.1707482954.57.0.1707482954.0.0.0; _ga_C3E4R66LJ8=GS1.1.1706739961.5.1.1706740024.60.0.0; _clck=1rczj7e%7C2%7Cfiv%7C0%7C1351; _gcl_aw=GCL.1707482953.CjwKCAiAt5euBhB9EiwAdkXWO2xVb8AMjzLvYewEsy2sS4RkLg4lYmHC-XaRWBf4U9MyLvMxp6DK8RoCX_UQAvD_BwE; _pxvid=a2c76bd3-5bbd-11ee-a0f8-aa3c30683e22; __pxvid=a30ca4f5-5bbd-11ee-910d-0242ac120003; _gac_UA-378501-55=1.1707482954.CjwKCAiAt5euBhB9EiwAdkXWO2xVb8AMjzLvYewEsy2sS4RkLg4lYmHC-XaRWBf4U9MyLvMxp6DK8RoCX_UQAvD_BwE; _gac_UA-378501-24=1.1707482956.CjwKCAiAt5euBhB9EiwAdkXWO2xVb8AMjzLvYewEsy2sS4RkLg4lYmHC-XaRWBf4U9MyLvMxp6DK8RoCX_UQAvD_BwE; _gac_UA-378501-51=1.1707482954.CjwKCAiAt5euBhB9EiwAdkXWO2xVb8AMjzLvYewEsy2sS4RkLg4lYmHC-XaRWBf4U9MyLvMxp6DK8RoCX_UQAvD_BwE; _gac_UA-378501-53=1.1707482954.CjwKCAiAt5euBhB9EiwAdkXWO2xVb8AMjzLvYewEsy2sS4RkLg4lYmHC-XaRWBf4U9MyLvMxp6DK8RoCX_UQAvD_BwE; _ga_LFTL75YJRF=GS1.1.1706743242.11.0.1706743246.0.0.0; ABTasty=uid=sy09ww4h5wf10t49&fst=1696533859760&pst=1702938443489&cst=1703087529664&ns=8&pvt=9&pvis=1&th=; _gcl_au=1.1.31369115.1709571837; TS017e8d10=01d053253db2d3c838f54e8ed8e8095a1b323f2ce0386f5d1c20d91a55ac22f0f2bb3fe81f40a93f088671f2cadba50788a83809df; dtCookie=v_4_srv_41_sn_8MP7HL313KU2Q3AM86VFV8A9GPB4TP0D_app-3A43a5284704382d12_1_ol_0_perc_100000_mul_1_rcs-3Acss_0; dtPC=41$442514298_484h6vQPFHBVUEKWOCMKPGONOPJWNLHEEFIQLG-0e0; rxvt=1709844314385|1709842463558; dtSa=-; pxcts=4a362694-dcbf-11ee-8e19-89f1ecb01821; TS01cc7ea9=01d053253db2d3c838f54e8ed8e8095a1b323f2ce0386f5d1c20d91a55ac22f0f2bb3fe81f40a93f088671f2cadba50788a83809df; TSe3289311027=08e7f9c7e6ab20000c0a6225bcf46514739720960549ac8af945ca9e0cb0a7a326b7c678554fb2210871826d55113000e23183cc4d3f7b3172a944d532bf6b35b559e0d0e5a427d51e1620ae63b7d65d74bf16f65871a122046c2064fd86af7f; _px3=ef17fe6d3bfbfe45d43e4da74f48c8bc5b8e79347c3fd64c911ad22362ac34a4:F4VVg5VWYSbHp51G7ac3suwGFQCmddUq4GDrzDBm3G93AJTo8IJMPchkEJFCsrDSSY+326iLHIlgb4ueRpxYVQ==:1000:qPL/TbTxNQop3B51k/o8IdTPokbnviU5KfVMwEnJzHNFZKZDBR38821WNpWJI4++2JqPnQi59lolmSh7oVFsrffUXEFgRpDrG9AVMWJQCakjrCMs52QtFFa8C70atIce63Lvtg0TiLDHxNGATIaUTw4vhii5BeK0ohDxcEWSltihfGsbuPc7v1CNMN1Oge27OKTY32m37CVcdKoFrGketT/TYFP2ci59WOgyyxiuQ0g=; _gid=GA1.2.1776783388.1709842465; _gat_UA-378501-55=1; _uetsid=4b44c510dcbf11eeb9c6f15adb315ea5; _uetvid=3067340048f611eea1333561af80a647; fs_lua=1.1709842466678",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}

price_data = []
# Realizar la solicitud para cada SKU en la lista
for sku, value in skus.items():
    url = base_url + str(value)
    response = requests.get(url, params=query_params, headers=headers)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        data = response.json()
        try:
            normal_price = data["price"]["BasePriceReference"]
            offer_price = data["price"]["BasePriceSales"]
            print(f"Normal Price {sku}: {normal_price}")
            print(f"Offer Price {sku}: {offer_price}")
            price_data.append([sku, normal_price, offer_price])
        except Exception as e:
            print(f"Error obteniendo precios para {sku}: {e}")
    else:
        print(f"SKU {sku} no es válido.")

# Enviar los datos a Google Sheets
values = price_data
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='Lider!A2:C',  # Rango de celdas donde se insertarán los datos
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

print("Datos insertados correctamente en Google Sheets")


time.sleep(0.5)       

end_time = time.time()  # Tiempo de finalización de la ejecución
execution_time = end_time - start_time
print("Tiempo de ejecución: %.2f segundos" % execution_time) 

now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
data = {"":now_str}
json_data = json.dumps(data)
values = [[json_data]]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                            range='Lider!D2',#CAMBIAR
                            valueInputOption='USER_ENTERED',
                            body={'values':values}).execute()     