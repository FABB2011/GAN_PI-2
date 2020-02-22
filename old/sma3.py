import numpy as np
from scipy.io import wavfile
import json
import math
import os
import pandas as pd
import matplotlib.pyplot as plt
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

def normalize(array):
    for i in range(len(array)):
        mean = np.mean(array)
        std = np.std(array)
        array[i] = (array[i] - mean) / std
    return array

def new_json(my_list, file_name, count):
    classes = [[0, -0.008652554295271312], [7, 0.027512441618893296], [9, 0.006449831802576555],
               [11, -0.0020621500033374835], [17, 0.007705425700149263], [19, 0.004555458556914246],
               [21, 0.0035467316260172892], [22, 0.007651164622245094], [23, 0.004915791862473162],
               [24, 0.005800564972365071], [29, -0.0343420390811666], [30, 0.0019084715324149764],
               [31, 0.012760648935090345], [35, -0.020291321431656476], [40, 0.0034815803224052346],
               [42, -0.00678427910443489], [43, 0.006421320864041189], [46, 1.2278101924797213],
               [47, 0.004441613319507986], [50, 0.03837800440492338], [51, 0.016931238241963083],
               [52, -0.0025048324259983558], [53, 0.005859911270715026], [55, 0.3550835992632258],
               [56, -0.0028466845092118107], [58, 0.0035203556034484195], [59, 0.002801666207572056],
               [60, 0.004008067240785877], [61, 0.013539427120059306], [63, 0.002861780031133427],
               [64, -0.42039474565995116], [65, 0.006675036192223575], [70, 0.002379844940861996],
               [76, 0.002152432219734411], [84, 0.003494689901786528], [87, 0.004406805166093968],
               [89, -0.043952258850928], [90, 0.010759976617006188], [94, 0.007224496602984706],
               [102, 0.06701619536367287], [103, 0.05027924226582581], [105, 0.0031540982384444904],
               [107, 0.025720330463803738], [108, -0.6034823645239573], [109, 0.0036026061337138685],
               [111, 0.010018295278371475], [114, 0.01434410113795207], [115, 0.0027992143280483085],
               [117, -0.0026578579265977282], [121, -0.13125016970411355], [123, 0.0034743989187859467],
               [126, 0.00188221948263834], [130, 0.009888132564750672], [131, -0.006201146142165983],
               [132, 0.005131367463479458], [134, 0.01712224091090184], [135, 0.03334789035747547],
               [142, 0.0027040556332219123], [148, 0.003934839998046368], [149, 0.01627452599174204],
               [154, -0.004267742767044483], [155, -0.027932513746150314], [159, 0.00929311939759941],
               [162, 0.004861799168901531], [177, 0.0023435065973579842], [180, 0.0023291865056481505],
               [186, 0.005925701060915897], [187, 0.011257562797339535], [191, 0.0066126710860611],
               [193, 0.02424010410122425], [194, 0.0015437940982599037], [209, 0.011782002957869204],
               [213, 0.00393985345010604], [219, -0.004250176894306189], [221, 0.008156462604318675],
               [225, 0.07549604166555256], [227, 0.0021339684599333457], [228, 0.0029779089550722596],
               [231, 0.01120195564498337], [232, 0.003580911331345971], [234, 0.001652876841459421],
               [235, 0.0007120585794110636], [251, -0.00805727325681657], [252, -0.005670714364952775],
               [253, 0.003474703758720655], [259, 0.01820712655615611], [262, 0.00395103760858335],
               [277, 0.021583513271955394], [278, 0.010871476467143433], [281, 0.03649354449010141],
               [283, -0.00827327495777033], [284, 0.4013024552822956], [285, 0.004009908430650072],
               [288, 0.004462265319563785], [290, -0.002936914279807107], [294, 0.06491774874593836],
               [297, 0.002994310339764456], [299, -0.0032646081219915423], [300, 0.04683537891155806],
               [306, 0.006218149418384502], [310, -0.0031395056281344684], [312, 0.0075242348865665245],
               [314, 0.0021087875774376008], [315, 0.015050910955699841], [316, -0.003546187673194109],
               [325, 0.009118663353795275], [327, 0.012601325902836635], [328, 0.0018495155905099883],
               [333, 0.004729969470242609], [334, 0.0251828705045085], [342, 0.004519771782834054],
               [344, -0.004796758106076885], [346, -0.013445462974536127], [348, 0.016428055068808678],
               [349, 0.011262117419697137], [354, 0.002589189963273343], [355, -0.00632307400761607],
               [367, 0.0036457919670482876], [370, 0.0034427260969795673], [386, 0.005719309899828844],
               [391, -0.006729923640490862], [392, -0.0018385570596547813], [394, 0.004829409041573565],
               [399, 0.003489068504151634], [404, 0.0027332415297738584], [409, -0.008108334246031168],
               [411, 0.006976042392124354], [415, 0.0027099797233998846], [417, 0.007514477214465686],
               [418, 0.0009667091212195322], [422, 0.0031123712134158953], [423, -0.006254019136102354],
               [425, 0.03506953007706455], [426, 0.012274367456397556], [430, 0.015156097323354245],
               [441, 0.0008359651770939512], [443, 0.0029083086846305303], [448, 0.015130746461055292],
               [449, 0.0037075748957575757], [452, 0.013986036250478546], [454, -0.005336411744061248],
               [455, 0.0064742466386736724], [456, 0.04329917899466005], [457, 0.008801033475986552],
               [459, 0.04968420726840341], [465, 0.0161580466308374], [467, 0.007740920862911472],
               [473, 0.002147446959975739], [474, 0.0021187006987079234], [475, 0.004644187742379164],
               [477, 0.007517720195931183], [478, 0.004352987230382962], [481, 0.004637017314401144],
               [482, 0.005036336094102705], [483, 0.00444829645123641], [487, 0.03801123474315756],
               [488, 0.017242881482270548], [497, 0.008361441971695943], [499, 0.0061790100064496485],
               [501, 0.0095140775984718], [503, 0.010769526314907756], [505, 0.0017112827658816734],
               [508, -0.007999877452856623], [511, 0.003899802570575651], [515, 0.0010951296198605561],
               [518, 0.027710040471049094], [521, 0.003906756696412319], [524, 0.0015756108754665786],
               [525, 0.004283609973995585], [527, 0.007352433554778099], [535, 0.02712796468771478],
               [537, 0.036954480034856935], [547, 0.01092815126960844], [551, 0.021604289432674943],
               [552, -0.023992110041934585], [553, 0.006172709290609759], [554, -0.017596127659166787],
               [556, -0.0487872595663653], [557, 0.006510086357182453], [559, 0.00349686573853388],
               [562, 0.016505896063911625], [565, 0.031097018139121035], [566, 0.005595514267403538],
               [568, 0.010114292487436796], [570, 0.004335019032194989], [574, -0.0027664391859622468],
               [575, 0.003881601768465452], [578, 0.03272362109374988], [580, 0.007743598646481125],
               [584, 0.016371410362423927], [594, 0.003133658149043323], [601, 0.009398221598739594],
               [602, -0.0023207761553012216], [608, 0.00629735816939937], [610, 0.002205765554261347],
               [611, 0.0038696251998374567], [613, 0.0029670198706685507], [616, -0.010032517935591567],
               [624, 0.0019757135321524107], [626, 0.005501072671020875], [630, -0.006414998263085751],
               [635, 0.004759722168832884], [636, 0.0032097024002796016], [639, -0.003960860483524219],
               [640, 0.008873748960367467], [641, 0.003838478743614735], [643, 0.4227740112809311],
               [646, 0.0034511865241863143], [648, -0.004635476906889908], [649, 0.006380112103198419],
               [650, 0.019444837043366435], [656, 0.0049136415934821695], [661, 0.033380770706895914],
               [664, 0.0020585552030265935], [665, 0.019559668575948142], [669, 0.02298126205621301],
               [671, 0.0024493180438016613], [673, 0.0024410593665348313], [678, 0.01712562919443886],
               [679, 0.00754147780663766], [680, 0.007751820742337277], [682, 0.0061983386764792045],
               [686, 0.005187654470162709], [687, 0.012637380447750198], [691, -0.005927344583729477],
               [694, -0.00311650068106362], [698, 0.0024106176882808077], [701, 0.018564912328638335],
               [708, 0.00294121435820376], [711, 0.017688674796471605], [716, 0.0036376362157565763],
               [717, 0.24991175818973807], [719, 0.0031989972421667496], [721, 0.004057342503824647],
               [723, 0.009939657340526781], [724, 0.005971314752652071], [727, -0.008150674404244572],
               [728, 0.00222877489566076], [737, 0.007089461979117254], [741, -0.0056492171330062456],
               [742, 0.0032924854423927305], [743, 0.0037066670347814003], [744, 0.00501781773536652],
               [750, 0.0016623516521499294], [753, 0.0041235100963222405], [759, 0.0019855733358555257],
               [768, 0.007528941189155579], [769, -0.0035171156156295763], [774, 0.008471482849740405],
               [776, 0.004186673960492778], [784, -0.0019071997961557612], [785, 0.04138691920354912],
               [786, 0.003584121918069043], [788, 0.0030260134265733462], [793, 0.004385845803865658],
               [795, 0.01778111636470138], [801, -0.011462928954946773], [812, 0.0043863495438119585],
               [813, -0.018930821504421394], [814, 0.002713162290448415], [816, 0.0019525122246643492],
               [824, 0.006184470089177755], [825, -0.0015065906168120575], [833, 0.19351257576508585],
               [836, 0.003116620093132306], [837, 0.0009896481620498597], [845, 0.009502920285209798],
               [846, 0.003874084031105612], [847, 0.00484648033466115], [850, 0.009096459798633298],
               [857, 0.002044474432555924], [865, 0.004278989651551785], [866, 0.04997274169150265],
               [868, 0.006239733263360806], [872, 0.05131717587381432], [874, -0.010042535598505972],
               [876, 0.008095658075671865], [878, -0.2710479910140775], [879, 0.04910291520282083],
               [883, 0.026550437475027534], [885, 0.007816444136819067], [888, 0.002944190422011455],
               [889, 0.004596204414458708], [901, 0.0122005057580616], [903, 0.02204216409097036],
               [904, 0.006993339548189316], [905, 0.017627613325651135], [907, 0.004513524090843033],
               [911, 0.02608964878730364], [912, 0.06062067303690995], [913, 0.0038098722989581323],
               [916, -0.0046517616228449], [917, 0.04799747505775499], [920, 0.006659808550254116],
               [936, 0.00835784234012089], [937, 0.009326630785404424], [938, 0.01541349042357742],
               [939, -0.008160148232788994], [947, 0.021043498782037037], [949, 0.07640829911590342],
               [950, 0.004478158437428352], [953, 0.0036949624182463815], [957, 0.0036943005370082033],
               [958, 0.012266037580312458], [960, 0.0018936866793989875], [961, -0.005304183919809742],
               [968, 0.010070759866180999], [970, -0.028719510069441623], [971, 0.07527395082260745],
               [973, 0.0036339370261525396], [974, 0.011300392996193872], [976, 0.0052883717612822664],
               [977, 0.008636248517955155], [978, 0.003190971120860608], [980, 0.01788483948555082],
               [981, -0.01101055733126234], [982, 0.0027360202223089053], [983, 0.02201240856053855],
               [984, 0.0038898769362001404], [985, 0.0024205013598160843], [986, 0.005785825207350626],
               [987, -0.005647758957378965], [992, -0.05509729207104951], [993, 0.00654869463626594]]

    data = {"truncation": 0.69811178936518, 'latent': my_list,
                "classes": classes
            }
    with open(dir_path+'/jsonStore/' + str(file_name) + '.json','w') as outfile:
        json.dump(data, outfile)

def sma(data, period):
    j = next(i for i, x in enumerate(data) if x is not None)
    our_range = range(len(data))[j + period - 1:]
    empty_list = [None] * (j + period - 1)
    sub_result = [np.mean(data[i - period + 1: i + 1]) for i in our_range]
    return np.array(empty_list + sub_result)

rate, audio = wavfile.read('/home/fabrice/PycharmProjects/GANV2/audioFiles/subzero15.3.wav')
audio = np.mean(audio, axis=1)
duration = len(audio)/rate
frame_rate = 30
images = int(duration*frame_rate)
div = rate//frame_rate

tab = []
for i in range(images):
    data = abs(np.fft.rfft(audio[div * i:div * (i+1)]))
    data = data.tolist()
    tab.append(data)

tabInv = []
for i in range(len(tab[0])):
    tabEq = []
    for j in range(images):
        tabEq.append(tab[j][i])
    tabInv.append(tabEq)

for i in range(len(tabInv)):
    tabInv[i] = tabInv[i]
    #tabInv[i] = sma(tabInv[i], 10)
    tabInv[i] = pd.DataFrame(tabInv[i])
    tabInv[i] = tabInv[i].ewm(span=10).mean()
    tabInv[i] = tabInv[i][0]

dataF = []
for i in range(images):
    tabT = []
    for j in range(len(tabInv)):
        tabT.append(tabInv[j][i])
    dataF.append(tabT)

for i in range(images):
    data = dataF[i][100:228]
    data = 2 * ((data - min(data)) / (max(data) - min(data))) - 1
    random.Random(5).shuffle(data)

    with open('/home/fabrice/PycharmProjects/GANV2/dataFiles/' + str(i) + '.txt', 'w') as f:
        for item in data: f.write("%s\n" % item)
    data = data.tolist()
    new_json(data, str(i), i+1)
