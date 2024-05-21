#No olvidarse del key.json
#Buscar todos los "Cambiar" antes de usar
#En chatgpt cruzar sku_dotu con links. Pedir que te haga el json desde el info del sheets
import json
import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

#Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json' #Cambiar check
SPREADSHEET_ID = '1LnQY2tABOaIN86_q80p24RNGFR3h_eTI9JVOF6HfeB4' #Cambiar check
creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


# PATH = "C:\\Program Files (x86)\\chromedriver.exe"
PATH = "/usr/local/bin/chromedriver"
# Configurar las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ver el Navegador
chrome_options.add_argument("--window-size=1920x1080")
start_time = time.time()  # Tiempo de inicio de la ejecución
driver = webdriver.Chrome(options=chrome_options)


sku2= {"GALL25": "https://super.eltit.cl/products/galleta-donuts-100gr-leche"} #Cambiar check
sku={
    "ALIM204": "https://super.eltit.cl/products/arena-sanitaria-2kg-master-cat-ecologica/",
    "BEBI219": "https://super.eltit.cl/products/bebida-2-0lt-pepsi-zero/",
    "CERE248": "https://super.eltit.cl/products/cereal-zucaritas-300gr/",
    "CERV251": "https://super.eltit.cl/products/cerveza-cuello-negro-330cc-ambar/",
    "CERV252": "https://super.eltit.cl/products/cerveza-cuello-negro-330cc-stout/",
    "GALL297": "https://super.eltit.cl/products/galleta-obsesion-85gr-menta/",
    "ASEO343": "https://super.eltit.cl/products/lavaloza-quix-bio-activos-limon-750-ml/",
    "ABAR379": "https://super.eltit.cl/products/nutella-350gr/",
    "BELL396": "https://super.eltit.cl/products/elite-panuelo-desechable-menta-3-h-6-un/",
    "VINO483": "https://super.eltit.cl/products/vino-castillo-res-750cc-merlot/",
    "CONF591": "https://super.eltit.cl/products/chubi-150gr-doypack/",
    "ABAR592": "https://super.eltit.cl/products/chuchoca-oso-500gr",
    "ABAR617": "https://super.eltit.cl/products/esencia-cola-mono-gourmet-100ml/",
    "ABAR626": "https://super.eltit.cl/products/flan-daily-20gr-caramelo/",
    "CONG640": "https://super.eltit.cl/products/congelado-habas-500gr-frutos-del-maipo/",
    "ABAR645": "https://super.eltit.cl/products/harina-oso-1kg-tostada/",
    "ABAR658": "https://super.eltit.cl/products/infusion-twinings-10u2gr-wberries/",
    "ASEO659": "https://super.eltit.cl/products/jabon-le-sancy-750-ml-frutos-rojos/",
    "CERV719": "https://super.eltit.cl/products/ce-cristal-350cc18u/",
    "VINO836": "https://super.eltit.cl/products/vino-pipeno-copahue-1-5lt/",
    "VINO839": "https://super.eltit.cl/products/vino-toro-piedra-750cc-sauvignon-blanc/",
    "LICO846": "https://super.eltit.cl/products/whisky-blenders-pride-1lt/",
    "ABAR847": "https://super.eltit.cl/products/yerba-pipore-250gr/",
    "Abar902": "https://super.eltit.cl/products/aceite-maravilla-chef-1lt-301299/",
    "BEBI919": "https://super.eltit.cl/products/bebida-591ml-coca-cola/",
    "BEBI924": "https://super.eltit.cl/products/agua-benedictino-6-5lt/",
    "BEBI927": "https://super.eltit.cl/products/bebida-591ml-coca-zero/",
    "ABAR1050": "https://super.eltit.cl/products/nachos-p-villa-180gr-queso/",
    "QUES1140": "https://super.eltit.cl/products/quesillo-colun-con-sal-bolsa-350gr/",
    "SNAC1147": "https://super.eltit.cl/products/pasas-morenas-mp-100grs/",
    "GALL25": "https://super.eltit.cl/products/galleta-donuts-100gr-leche",
    "LICO194": "https://super.eltit.cl/products/licor-araucano-900cc-28-c2-a7",
    "PANA197": "https://super.eltit.cl/products/pan-molde-integral-con-masa-madre-fuchs-650gr",
    "SNAC205": "https://super.eltit.cl/products/p-fritas-mp-185gr-rustica-merquen",
    "CONS206": "https://super.eltit.cl/products/barilla-pesto-alla-genovese",
    "JUGU207": "https://super.eltit.cl/products/pila-duracell-d-2unidades",
    "FRUT208": "https://super.eltit.cl/products/bolsa-platano-1kg-aprox",
    "ABAR212": "https://super.eltit.cl/products/caldo-polvo-48gr-carne/",
    "CONF214": "https://super.eltit.cl/products/choc-ritter-100gr-mazapan/",
    "CONF216": "https://super.eltit.cl/products/choc-ritter-100gr-mazapan/",
    "Abar232": "https://super.eltit.cl/products/chips-chocolate-blanco-200gr-gourmet",
    "LACT245": "https://super.eltit.cl/products/yog-protein-soprole-155gr-frutilla",
    "LICO247": "https://super.eltit.cl/products/fernet-branca-750cc-menta",
    "ASEO262": "https://super.eltit.cl/products/suavizante-soft-1-lts-normal",
    "LACT266": "https://super.eltit.cl/products/leche-soprole-1lt-gold-cappuccino",
    "HELA275": "https://super.eltit.cl/products/cassata-savory-1lt-pina",
    "CERE282": "https://super.eltit.cl/products/cereal-nestle-corn-flakes-480gr",
    "BEBI288": "https://super.eltit.cl/products/energetica-monster-473ml-energy-s",
    "GALL289": "https://super.eltit.cl/products/galletas-crackelet-costa-85gr",
    "BEBI290": "https://super.eltit.cl/products/bebida-1-5lt-tonica-lg/",
    "BEBI291": "https://super.eltit.cl/products/agua-pellegrino-330cc-limonata-2/",
    "VINO303": "https://super.eltit.cl/products/vino-toro-piedra-750cc-carmenere/",
    "VINO309": "https://super.eltit.cl/products/vino-toro-piedra-750cc-cabernet/",
    "ABAR321": "https://super.eltit.cl/products/aceite-natura-900ml/",
    "BEBI323": "https://super.eltit.cl/products/agua-benedictino-2lt-cg-2/",
    "ALIM324": "https://super.eltit.cl/products/pedigree-cachorro-e1-3-kg/",
    "ABAR325": "https://super.eltit.cl/products/arroz-miraflores-1kg-g1-lam/",
    "CONS337": "https://super.eltit.cl/products/atun-vam-camps-160gr-aceite/",
    "CONS341": "https://super.eltit.cl/products/atun-vam-camps-160gr-agua/",
    "CONS346": "https://super.eltit.cl/products/atun-otuna-160gr-aceite/",
    "CONS347": "https://super.eltit.cl/products/atun-otuna-160gr-agua/",
    "BEBI349": "https://super.eltit.cl/products/desch-1-5-coca-cola/",
    "BEBI351": "https://super.eltit.cl/products/desch-1-5-coca-zero/",
    "BEBI352": "https://super.eltit.cl/products/bebida-3-0lt-pepsi-zero/",
    "CONS353": "https://super.eltit.cl/products/bruschetta-alcachofa-p-choice/",
    "ABAR354": "https://super.eltit.cl/products/cafe-copacabana-mol-250gr/",
    "ABAR357": "https://super.eltit.cl/products/nescafe-trad-tarro-170gr/",
    "CERE359": "https://super.eltit.cl/products/barra-de-cereal-en-linea-proteina-cranberries/",
    "SNAC365": "https://super.eltit.cl/products/castana-caju-mp-80gr-alum/",
    "CERE377": "https://super.eltit.cl/products/cereal-chocapic-receta-original-330gr/",
    "CERE382": "https://super.eltit.cl/products/cer-avena-quaker-inst-500gr-2/",
    "CONG385": "https://super.eltit.cl/products/cong-f-maipo-500gr-choclo-grano/",
    "CONG386": "https://super.eltit.cl/products/congelado-choclo-400gr-la-crianza/",
    "CONF390": "https://super.eltit.cl/products/choc-sahne-nuss-160gr-trad/",
    "CONF393": "https://super.eltit.cl/products/choc-sahne-nuss-250gr-bitter/",
    "CONF397": "https://super.eltit.cl/products/choc-trencito-150gr/",
    "FRUT400": "https://super.eltit.cl/products/bolsa-cilantro-1u/",
    "LACT401": "https://super.eltit.cl/products/crema-colun-1lt-base/",
    "ASEO402": "https://super.eltit.cl/products/detergente-liquido-ariel-tod-concentrado-1-9-lt/",
    "VINO409": "https://super.eltit.cl/products/espumante-misiones-750cc-brut/",
    "VINO410": "https://super.eltit.cl/products/sparkling-misiones-750cc-rose/",
    "CONG411": "https://super.eltit.cl/products/iqf-filete-pechuga-pollo-700gr/",
    "JUGU412": "https://super.eltit.cl/products/fosforos-copihue-10-un/",
    "GALL418": "https://super.eltit.cl/products/galleta-bon-o-bon-95gr/",
    "GALL419": "https://super.eltit.cl/products/galleta-tuareg-120gr/",
    "GALL439": "https://super.eltit.cl/products/galleta-donuts-100gr-orange/",
    "GALL443": "https://super.eltit.cl/products/galleta-obsesion-85gr/",
    "GALL445": "https://super.eltit.cl/products/galleta-selz-107gr-cracker/",
    "CONS451": "https://super.eltit.cl/products/garbanzo-esmeralda-400gr/",
    "PANA465": "https://super.eltit.cl/products/hallulla-1kg-aprox/",
    "HARI470": "https://super.eltit.cl/products/harina-mont-blanc-1kg-s-polvo/",
    "HARI474": "https://super.eltit.cl/products/harina-selecta-1kg-c-p/",
    "HARI477": "https://super.eltit.cl/products/harina-selecta-1kg-s-p/",
    "HARI481": "https://super.eltit.cl/products/harina-selecta-5kg-s-p/",
    "BELL482": "https://super.eltit.cl/products/jabon-elite-700ml/",
    "CONS485": "https://super.eltit.cl/products/jurel-san-jose-medallon-425gr/",
    "LACT494": "https://super.eltit.cl/products/leche-colun-1lt-base-choc-original/",
    "LACT507": "https://super.eltit.cl/products/leche-colun-1lt-base-descremada/",
    "LACT509": "https://super.eltit.cl/products/leche-colun-1lt-semidescremada/",
    "LICO515": "https://super.eltit.cl/products/jagermeister-700ml/",
    "FRUT527": "https://super.eltit.cl/products/bolsa-limon-1kg-aprox/",
    "SNAC529": "https://super.eltit.cl/products/mani-mp-miel-150gr/",
    "LACT530": "https://super.eltit.cl/products/mantequilla-untable-pote-200gr/",
    "ABAR531": "https://super.eltit.cl/products/mayonesa-kraft-397gr/",
    "BEBI532": "https://super.eltit.cl/products/shampoo-pantene-400ml-restauracion/",
    "CERV540": "https://super.eltit.cl/products/cerveza-corona-330cc6u/",
    "CONS548": "https://super.eltit.cl/products/c-palmito-esmeralda-400gr-rodaja/",
    "CONS552": "https://super.eltit.cl/products/c-palmito-esmeralda-400gr-ent/",
    "PANA553": "https://super.eltit.cl/products/pan-blanco-ideal-xl/",
    "SNAC556": "https://super.eltit.cl/products/p-fritas-mp-185gr-rustica-merquen/",
    "ASEO580": "https://super.eltit.cl/products/ph-elite-ultra-dh-25mt-4u/",
    "CONS583": "https://super.eltit.cl/products/pina-esmeralda-567gr/",
    "LICO585": "https://super.eltit.cl/products/pisco-alto-carmen-1-5lt/",
    "CONS586": "https://super.eltit.cl/products/porotos-negros-wasil-380gr-311147/",
    "QUES595": "https://super.eltit.cl/products/queso-philadelphia-crema-210gr__trashed/",
    "QUES596": "https://super.eltit.cl/products/queso-gouda-500gr-soprole/",
    "QUES597": "https://super.eltit.cl/products/queso-mantecoso-quilque-250gr/",
    "BELL611": "https://super.eltit.cl/products/shampoo-pantene-400ml-micelar/",
    "CONF620": "https://super.eltit.cl/products/choc-super-8-oblea-29gr/",
    "BELL624": "https://super.eltit.cl/products/th-ladysoft-noct-7u-malla-96280/",
    "ASEO627": "https://super.eltit.cl/products/th-babysec-premium-45unid-73117/",
    "VINO629": "https://super.eltit.cl/products/vino-castillo-res-750cc-cab-sauv/",
    "VINO630": "https://super.eltit.cl/products/vino-castillo-res-750cc-carmenere/",
    "VINO636": "https://super.eltit.cl/products/vino-dark-red-750cc/",
    "LICO638": "https://super.eltit.cl/products/whisky-ballantines-700cc-7anos/",
    "BEBI654": "https://super.eltit.cl/products/agua-voss-800cc-sgas/",
    "LICO676": "https://super.eltit.cl/products/ramazzotti-700cc-violetto/",
    "BEBI677": "https://super.eltit.cl/products/desch-3lt-fanta/",
    "BEBI679": "https://super.eltit.cl/products/bebida-3-0lt-pet-kem/",
    "BEBI686": "https://super.eltit.cl/products/bebida-500cc-kem-pina/",
    "BEBI690": "https://super.eltit.cl/products/bebida-3-0lt-pet-limon-soda/",
    "CONF691": "https://super.eltit.cl/products/choc-rocher-t8-100gr/",
    "ABAR692": "https://super.eltit.cl/products/cafe-nescafe-decafeinado-170gr/",
    "ABAR693": "https://super.eltit.cl/products/cd-sobre-callampas-goumet-35gr/",
    "HELA715": "https://super.eltit.cl/products/cassata-chamonix-2-5-lt-pina/",
    "QUES732": "https://super.eltit.cl/products/queso-chacra-sin-lactosa-400gr-quillayes/",
    "CONF740": "https://super.eltit.cl/products/milky-way-singles-52gr/",
    "ASEO744": "https://super.eltit.cl/products/cif-crema-bioactive-750gr-original",
    "ABAR749": "https://super.eltit.cl/products/cd-sobre-clavo-olor-ent-gourmet-5gr/",
    "ABAR757": "https://super.eltit.cl/products/cd-sobre-clavo-olor-mol-gourmet-5gr/",
    "GALL764": "https://super.eltit.cl/products/emparedado-ecovida-150gr-frutilla/",
    "VINO777": "https://super.eltit.cl/products/espumoso-valdivieso-750cc-brut/",
    "ABAR787": "https://super.eltit.cl/products/fideos-carozzi-400gr-spag5-carozzi",
    "GALL789": "https://super.eltit.cl/products/gall-mckay-120gr-coco/",
    "CONF793": "https://super.eltit.cl/products/galleta-morocha-240gr-familiar/",
    "CONF802": "https://super.eltit.cl/products/gomita-fini-90gr-gusano-acido/",
    "ASEO811": "https://super.eltit.cl/products/virutex-guante-s-mediano/",
    "ABAR817": "https://super.eltit.cl/products/humo-gourmet-liq-165cc/",
    "LACT829": "https://super.eltit.cl/products/leche-l-vida-soprole-200ml-chocolate/",
    "LACT830": "https://super.eltit.cl/products/leche-colun-1lt-frutilla-base/",
    "LACT831": "https://super.eltit.cl/products/leche-l-leche-sin-lactosa-l-1lt",
    "ASEO835": "https://super.eltit.cl/products/limpiador-glassex-multiuso-gatillo-500-ml/",
    "ASEO840": "https://super.eltit.cl/products/lustra-muebles-250-ml-virginia/",
    "SNAC842": "https://super.eltit.cl/products/mani-evercrips-100gr-japones/",
    "BEBI844": "https://super.eltit.cl/products/nectar-watts-1-5lt-damasco/",
    "AUTO845": "https://super.eltit.cl/products/panceta-ahumada-pf-150gr/",
    "LICO850": "https://super.eltit.cl/products/pisco-campanario-700cc-mango/",
    "CONG852": "https://super.eltit.cl/products/cong-poroto-verde-350gr-f-maipo/",
    "PANA856": "https://super.eltit.cl/products/quesavilla-pancho-villa-200gr/",
    "QUES860": "https://super.eltit.cl/products/queso-parmesano-sachet-soprole-80gr/",
    "ABAR864": "https://super.eltit.cl/products/salsa-tom-lucheti-200gr-natural",
    "ABAR867": "https://super.eltit.cl/products/sopa-maggi-70gr-pollo-fideos/",
    "BELL869": "https://super.eltit.cl/products/th-donnaset-maternidad-suave-2/",
    "VINO870": "https://super.eltit.cl/products/vino-carmen-700cc-merlot/",
    "VINO872": "https://super.eltit.cl/products/vino-e-chile-750ml-carmenere-2/",
    "VINO876": "https://super.eltit.cl/products/vino-misiones-cuvee-750cc-carmenere/",
    "VINO877": "https://super.eltit.cl/products/vino-m-rengo-rva-750cc-carmenere/",
    "VINO878": "https://super.eltit.cl/products/vino-montes-alpha-750cc-cab-sauv/",
    "VINO879": "https://super.eltit.cl/products/vino-undurraga-pinot-750cc-cab-sauv/",
    "VINO881": "https://super.eltit.cl/products/vino-sta-helena-2lt-blanco/",
    "VINO882": "https://super.eltit.cl/products/vino-export-sel-1-5lt-bot-carmenere/",
    "VINO883": "https://super.eltit.cl/products/vino-gran-rva-750cc-cab-sauv/",
    "LICO884": "https://super.eltit.cl/products/whisky-jack-daniels-750cc-honey/",
    "LACT887": "https://super.eltit.cl/products/yog-nestle-cereal-142gr-trix-c-c/",
    "LACT888": "https://super.eltit.cl/products/yogurt-quillayes-griego-frutilla-triple-0-800-gr/",
    "LACT889": "https://super.eltit.cl/products/yogurt-sin-lactosa-de-vainilla-colun-125gr/",
    "Abar891": "https://super.eltit.cl/products/leche-conden-nestle-397gr-12001455/",
    "Abar892": "https://super.eltit.cl/products/mayonesa-hellmanns-sup-380gr-sin-marcas",
    "Abar898": "https://super.eltit.cl/products/salsa-pomarola-200gr-ital/",
    "Abar909": "https://super.eltit.cl/products/nescafe-trad-tarro-170gr",
    "Abar911": "https://super.eltit.cl/products/salsa-toscana-200gr-bolognesa/",
    "Abar912": "https://super.eltit.cl/products/salsa-tom-tuco-245gr-carne/",
    "Abar915": "https://super.eltit.cl/products/te-supremo-ceylan-prem-10100/",
    "Abar917": "https://super.eltit.cl/products/azucar-iansa-500gr-dorada/",
    "Abar918": "https://super.eltit.cl/products/fideos-carozzi-400gr-tall87/",
    "Abar920": "https://super.eltit.cl/products/leche-nido-buen-dia-700gr/",
    "Abar921": "https://super.eltit.cl/products/milo-450gr",
    "Abar922": "https://super.eltit.cl/products/chancaca-deliciosa-400gr/",
    "Abar923": "https://super.eltit.cl/products/cafe-cruzeiro-250gr-intenso-molido/",
    "Abar925": "https://super.eltit.cl/products/cafe-tarro-lavazza-250gr-qualita-oro/",
    "Abar926": "https://super.eltit.cl/products/te-supremo-ceylan-premium-2520/",
    "Abar928": "https://super.eltit.cl/products/te-supremo-mildred-ceylan-10100/",
    "Aseo929": "https://super.eltit.cl/products/servilleta-elite-50-un-mesa-22550/",
    "Aseo931": "https://super.eltit.cl/products/bolsa-basura-bio-80120cm-virutex/",
    "BEBI932": "https://super.eltit.cl/products/nectar-watts-1-5lt-lg-naranja/",
    "BEBI933": "https://super.eltit.cl/products/agua-cachantun-1-6lt-sin-gas/",
    "BEBI937": "https://super.eltit.cl/products/bebida-3-0lt-pepsi/",
    "BEBI941": "https://super.eltit.cl/products/red-bull-light-250-cc/",
    "BEBI946": "https://super.eltit.cl/products/nectar-watts-1-5lt-naranja/",
    "BEBI950": "https://super.eltit.cl/products/lata-350cc-coca-zero/",
    "BEBI951": "https://super.eltit.cl/products/red-bull-355-cc/",
    "BEBI953": "https://super.eltit.cl/products/red-bull-250-cc/",
    "BEBI954": "https://super.eltit.cl/products/nectar-watts-1-5lt-lg-pina/",
    "BEBI959": "https://super.eltit.cl/products/nectar-watts-1-5lt-lg-durazno/",
    "BEBI960": "https://super.eltit.cl/products/desch-1-5-fanta/",
    "BEBI962": "https://super.eltit.cl/products/nectar-watts-1-5lt-durazno/",
    "CERV964": "https://super.eltit.cl/products/heineken-350cc6u-lat/",
    "LICO965": "https://super.eltit.cl/products/tequila-olmeca-750cc-dark/",
    "CERV968": "https://super.eltit.cl/products/ce-coors-st-355cc6u/",
    "CERV977": "https://super.eltit.cl/products/ce-austral-470cc-lager-red/",
    "CONF978": "https://super.eltit.cl/products/rolls-150gr-crocante/",
    "CONF979": "https://super.eltit.cl/products/choc-sahne-nuss-250gr-bitter/",
    "CONF982": "https://super.eltit.cl/products/choc-rocher-150gr-t-12/",
    "CONF983": "https://super.eltit.cl/products/chocolate-rocher-100gr-t-08-corazon/",
    "CONF984": "https://super.eltit.cl/products/chocolate-costa-rama-115gr/",
    "CONF985": "https://super.eltit.cl/products/chocolate-golden-120gr/",
    "CONF986": "https://super.eltit.cl/products/choc-tobler-100gr-honey",
    "CONF987": "https://super.eltit.cl/products/chocolate-costa-62-100gr-menta",
    "CONF988": "https://super.eltit.cl/products/galleta-costa-maxi-200gr",
    "CONG989": "https://super.eltit.cl/products/cong-f-maipo-500gr-arveja",
    "LACT990": "https://super.eltit.cl/products/mantequilla-alerce-250gr",
    "LACT991": "https://super.eltit.cl/products/postre-manjarate-soprole-80gr",
    "LACT992": "https://super.eltit.cl/products/manjar-colun-bolsa-1kg",
    "LACT993": "https://super.eltit.cl/products/leche-colun-s-lactosa-1lt-edge-natural",
    "LACT994": "https://super.eltit.cl/products/leche-colun-200ml-chocolate-original",
    "LACT996": "https://super.eltit.cl/products/manjar-receta-campo-1kg",
    "LACT1000": "https://super.eltit.cl/products/yog-protein-soprole-155gr-frutilla",
    "LACT1013": "https://super.eltit.cl/products/yogurto-colun-1lt-frutilla",
    "LICO1014": "https://super.eltit.cl/products/vodka-absolut-750ml-blue",
    "LICO1016": "https://super.eltit.cl/products/aperol-750cc",
    "LICO1017": "https://super.eltit.cl/products/gin-beefeater-750cc",
    "LICO1018": "https://super.eltit.cl/products/pisco-alto-carmen-1lt",
    "LICO1020": "https://super.eltit.cl/products/pisco-alto-d-carmen-750cc-40g-trans",
    "QUES1024": "https://super.eltit.cl/products/queso-los-tilos-350gr-fresco",
    "VINO1026": "https://super.eltit.cl/products/vino-gato-2lt-tet-tinto/",
    "VINO1031": "https://super.eltit.cl/products/espumante-riccadonna-750cc-moscato-rose/",
    "VINO1034": "https://super.eltit.cl/products/vino-med-real-750cc-cab-sauv/",
    "VINO1038": "https://super.eltit.cl/products/vino-gato-1-5lt-bot-merlot/",
    "VINO1040": "https://super.eltit.cl/products/espumante-riccadonna-750cc-prosecco/",
    "VINO1044": "https://super.eltit.cl/products/vino-castillo-res-750cc-chard/",
    "VINO1048": "https://super.eltit.cl/products/vino-toro-piedra-750cc-carmenere/",
    "VINO1056": "https://super.eltit.cl/products/vino-gato-2lt-tet-blanco",
    "ABAR1060": "https://super.eltit.cl/products/base-gourmet-90gr-hamburguesas",
    "ABAR1064": "https://super.eltit.cl/products/te-twinings-10u2gr-lemon/",
    "ABAR1065": "https://super.eltit.cl/products/miel-palma-cocalan-330gr/",
    "ABAR1072": "https://super.eltit.cl/products/base-gourmet-80gr-pollo-crispy",
    "ABAR1076": "https://super.eltit.cl/products/sopa-gourmet-62gr-costilla-fideos",
    "ASEO1081": "https://super.eltit.cl/products/talco-books-pies-y-zapat-80gr",
    "AUTO1089": "https://super.eltit.cl/products/pate-rda-125gr-campo-wp",
    "BEBI1115": "https://super.eltit.cl/products/agua-voss-800cc-cgas",
    "BEBI1130": "https://super.eltit.cl/products/jugo-afe-200cc-tet-manzana",
    "BELL1132": "https://super.eltit.cl/products/des-rexona-clinical-48gr-woman-dry",
    "CONS1133": "https://super.eltit.cl/products/champinon-wasil-400gr-lam-311041/",
    "LACT1138": "https://super.eltit.cl/products/yog-griego-tzos-110gr-frutilla/",
    "QUES1155": "https://super.eltit.cl/products/queso-santa-rosa-150gr-ricotta/",
    "VINO1156": "https://super.eltit.cl/products/vino-anejo-s-blas-750cc/"
}

results = []

for sku_key, url in sku.items():
    driver.get(url)
    precio_oferta = "No disponible"
    precio_normal = "No disponible"
    try:
        # Intenta obtener el precio de oferta
        precio_oferta_element = driver.find_element("xpath", '/html/body/div[1]/div/section[1]/div[1]/div[2]/div/span[3]') #Cambiar
        precio_oferta = precio_oferta_element.text  # Guarda el precio de oferta
    except NoSuchElementException:
        pass  # Si no se encuentra el precio de oferta, se continuará con el siguiente bloque de código

    try:
        # Intenta obtener el precio normal
        precio_normal_element = driver.find_element("xpath", '/html/body/div[1]/div/section[1]/div[1]/div[2]/div/div[2]/span') #Cambiar
        precio_normal = precio_normal_element.text  # Guarda el precio normal
    except NoSuchElementException:
        pass  # Si no se encuentra el precio normal, se continuará con el siguiente bloque de código

    if precio_oferta == "No disponible" and precio_normal == "No disponible":
        try:
            # Si no se puede encontrar ni el precio de oferta ni el precio normal, intenta con el tercer XPath
            precio_normal_element = driver.find_element("xpath", '/html/body/div[1]/div/section[1]/div[1]/div[2]/div/div[2]/span') #Cambiar
            precio_normal = precio_normal_element.text  # Guarda el precio normal
        except NoSuchElementException as e:
            print(f"No se pudo encontrar el precio en la URL {url} - {e}")

    data = {
        "SKU": sku_key,
        "Precio": precio_normal,
        "Precio_oferta": precio_oferta
    }
    results.append(data)
    print(data)
    time.sleep(0.5)
driver.quit()


df = pd.DataFrame(results)

# Guardar el DataFrame en un archivo Excel
# nombre_archivo = "datos_productos.xlsx"  # Nombre del archivo Excel
# df.to_excel(nombre_archivo, index=False)  # El parámetro index=False evita que se incluyan los índices en el archivo Excel
# print(f"Datos guardados en {nombre_archivo}")


end_time = time.time()  # Tiempo de finalización de la ejecución
execution_time = end_time - start_time
print("Tiempo de ejecución: %.2f segundos" % execution_time)

#Fecha de Extraccion
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
data = {"":now_str}
json_data = json.dumps(data)
values = [[json_data]]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='eltit!J2',#CAMBIAR check
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()


#Valores que se pasan a Sheets
values = [[item['SKU'], item['Precio'],item['Precio_oferta']]for item in results]
result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
							range='eltit!A2:C1000',#CAMBIAR check
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente")
competitor = "eltit"  # Cambiar 


# Enviar datos a otro Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
NEW_SPREADSHEET_ID = '1y-NLrx7pewwMP1OGzLTZcpolTBkhiz5yZAhTohBGFKE'  # ID de la nueva hoja de cálculo

creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Obtener la última fila con datos en la nueva hoja
result = sheet.values().get(spreadsheetId=NEW_SPREADSHEET_ID, range='tejamarket!A:A').execute() #Cambiar donde llega la info
values = result.get('values', [])
last_row = len(values) + 1  # Obtener el índice de la última fila vacía

# Convertir resultados a la lista de valores
values = [[row['SKU'], competitor, row['Precio'], row['Precio_oferta'], now_str] for _, row in df.iterrows()]

# Insertar los resultados en la nueva hoja después de la última fila
update_range = f'tejamarket!A{last_row}:E{last_row + len(values) - 1}' #Cambiar
result = sheet.values().update(
    spreadsheetId=NEW_SPREADSHEET_ID,
    range=update_range,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()

print(f"Datos insertados correctamente en la nueva hoja de Google Sheets en el rango {update_range}")