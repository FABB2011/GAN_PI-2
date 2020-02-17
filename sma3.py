import numpy as np
from scipy.io import wavfile
import json
import math
import os
import pandas as pd
# import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))

def new_json(my_list, file_name):
    data = {"truncation": 0.7696946259947698, 'latent': my_list,
            #'classes': [[188, 0.2696612715283029], [338, 0.9262914142148885], [385, 0.13095440634023092], [483, 0.20723007243371555]]}
            "classes":[[1,0.006494872154618431],[2,-0.0031559476419899197],[3,0.007675554703073598],[4,0.0024732203474486575],[5,-0.002578394509938936],[7,-0.006380649947474356],[8,-0.023008451729916023],[9,0.006141084522960263],[12,0.005098222847688528],[14,-0.019574280197043194],[16,-0.004552264888066988],[17,0.021342244383115973],[18,0.005480297389240607],[19,-0.002157002870265489],[20,0.011175262862815193],[25,-0.006353300905686599],[28,0.002920055139478871],[29,-0.01780304988507115],[35,-0.005448781244072367],[36,0.006602494287026658],[37,-0.004141841133735836],[38,0.0429922355660792],[41,-0.004367244532667722],[46,0.005323906331983853],[49,0.004250476420585475],[50,-0.005609790182972068],[51,0.0044211818793852406],[52,-0.02087035157881737],[54,-0.002587692915967829],[55,-0.0036869091353735443],[56,-0.006118406005632453],[57,-0.005277489809358234],[60,-0.0038430141428790936],[66,-0.003933769431148031],[68,-0.0020626905401110447],[69,-0.004346538604050626],[70,-0.018002367639215],[71,-0.03910394499086271],[73,0.03000182023466693],[74,0.0041481663989575155],[78,-0.04717203624379395],[79,0.003703111305123608],[81,0.003075393709775334],[85,-0.0038449033778345486],[86,-0.0038473787817415914],[87,0.023010057754537194],[90,-0.11356714162109066],[92,0.009208470434630602],[93,0.006311031880816883],[94,-0.016560739919223452],[100,0.016208348173178844],[103,0.003084453076639612],[105,0.022621458954326865],[106,-0.003063528626435481],[107,0.06296128027424365],[108,0.024254092225013513],[109,0.015153447224248185],[110,-0.050796912573493766],[111,-0.009486339939687158],[112,0.007730877290939475],[113,0.010481167573268384],[114,0.005464029856845649],[115,-0.004400638295565718],[116,-0.005272221676168185],[117,-0.053723022611412305],[119,0.0052647132432840655],[120,0.007295999542290868],[121,0.020157499834668552],[122,0.0026412142920731393],[123,0.00504423833567915],[126,0.0038721849412665017],[127,-0.005124269444639017],[129,-0.003954455253903721],[130,0.004048463594321124],[131,0.009959700868562576],[132,-0.0052039103532173225],[134,0.004675796492581888],[135,-0.0030753881112425586],[143,0.003933518568038825],[146,-0.02352594972637894],[147,0.005186183672100764],[148,-0.031010253238259733],[149,0.004256546851987637],[150,0.00584083177867592],[154,0.0022698853928991925],[155,0.003194529686668286],[157,0.007343398095658712],[158,-0.005831678870453345],[161,0.007160328612722153],[163,-0.004940587484082814],[164,-0.004074886058945251],[169,-0.002981738369160527],[170,-0.0036714154030360988],[172,-0.003565672234814531],[176,-0.005762009611892],[177,-0.037336590433829586],[181,-0.0020233547823094813],[186,-0.0038957851253888474],[188,-0.018817581998148147],[189,0.008471205395667269],[191,0.003299827882277543],[192,-0.006040141460537841],[193,0.005892712175682161],[195,0.021957218254436476],[196,0.0031331556390763655],[200,-0.004081653352184906],[201,0.0023609964722193276],[202,0.0038939183202277962],[204,-0.005622909424378425],[205,0.0047524556523987575],[206,-0.004522619904977846],[209,-0.0077149357414515105],[212,0.048869649878750754],[213,0.005726865468257268],[215,-0.005179814554609733],[216,0.00390240596950198],[218,-0.004004636618224956],[219,0.0025837733012546897],[221,0.0045893692950107765],[223,0.009052124666317739],[224,-0.0031531043754991417],[227,-0.003354938570171522],[230,-0.01828150216571333],[232,-0.006354368299303376],[236,-0.006004004787373434],[237,-0.03994976817273199],[240,-0.003996537348386756],[241,-0.007294989397369353],[247,-0.00409093240898392],[249,-0.004028365034746767],[251,0.12392148241907468],[253,0.006854275835789977],[254,0.02675761754876034],[255,-0.003991801353983735],[258,0.03222106081126723],[261,-0.002906001280119568],[262,-0.005340107518566335],[264,0.002819484051786252],[268,-0.003515591567692912],[269,-0.0017622483906657668],[270,-0.0049444841963681985],[273,-0.003969064719466748],[278,-0.0024163676353934323],[279,-0.004262331049787529],[281,-0.026095301730992955],[282,0.09604456676131465],[283,0.14411536673873143],[286,0.005718065224560061],[287,0.001501735391159159],[288,0.00556279009195971],[289,-0.005057950022813673],[290,-0.004247464866723328],[291,-0.0026683096770358187],[295,-0.0097149676682653],[296,-0.0101047681461463],[306,-0.0031729366873390593],[309,0.0049272747084188745],[314,0.003781159827027064],[315,0.005656131891931112],[316,0.002566123773474392],[323,0.01645630225409215],[324,-0.0035013701470774554],[325,-0.004081545639799989],[327,0.005979493134303993],[329,-0.009959017155585384],[333,0.007714618109981936],[334,0.667550346600656],[338,-0.009382286273940891],[339,0.08870588629827914],[341,0.004711562012316865],[344,-0.006205126450837266],[347,-0.003826498323744638],[348,0.004109727852148259],[350,0.0038546659262717045],[354,-0.005390700444674011],[356,0.02251609109714366],[360,-0.018077316443501308],[361,0.00359647875405936],[363,-0.0055149224364463255],[366,-0.12347952495328521],[368,0.025437554046467276],[369,-0.00350922790132799],[370,-0.0064691959306322575],[376,0.00420163929247789],[377,-0.0037652119424283464],[381,0.45997945832546605],[383,-0.007005446840727238],[384,-0.003415941722936605],[385,-0.011626652433938558],[386,-0.007443325245702454],[387,0.03342121133160094],[390,-0.008565030639405204],[393,0.00741672032663562],[394,0.0019331246761482158],[396,-0.006363687429237775],[397,0.0408244115876783],[398,-0.03713500975283299],[399,0.006394881593444709],[402,-0.004107431039845973],[403,-0.007773071910093854],[404,-0.00829280600965017],[405,0.010743455531943849],[409,-0.0134980562412857],[410,-0.03669486123999153],[413,0.004756222479933129],[417,0.010583702900172319],[419,0.013808916249443462],[420,-0.08257238379278735],[425,0.04067595711419821],[433,-0.004483017876575953],[434,-0.009426822354547875],[435,0.008840846939828843],[438,0.011524987708335578],[439,-0.003966417866360131],[440,0.001834588629190215],[443,0.011950633504632383],[445,0.007790241784444955],[448,0.1895652845670765],[451,0.004324513134124603],[452,-0.2515654682084555],[454,-0.006600150654253744],[456,-0.10594759835363465],[459,0.015615476233998223],[462,-0.005106502236172521],[464,0.029704034539605698],[465,-0.00448189706953934],[468,0.008133176073691229],[470,-0.002745212891032149],[471,0.002193312679427079],[476,0.024946347646736804],[479,0.01830089405050799],[482,0.0019796200501018546],[483,0.008958921434213486],[487,-0.0052717658291390685],[488,0.2780583642559588],[490,0.005218143769738273],[491,0.004899216483931968],[493,-0.004219583855637958],[497,0.20973763769936032],[499,0.03100625282582047],[500,0.016882198720235612],[501,0.004572616982877082],[508,0.02410180615381538],[510,-0.0033527100802285105],[513,0.003534289766002458],[515,0.004039619564520705],[516,-0.00235359319587091],[518,0.005298125454145325],[519,0.006564378650463255],[520,-0.003978576937017742],[521,0.0033136783027931135],[522,0.005991412858862346],[524,0.007586931850890555],[525,-0.006554473933053978],[530,0.025510061317139184],[532,-0.009627697570396207],[533,-0.00455273185205216],[538,0.006430784896134767],[545,0.006920298285537321],[549,-0.0038892941120288165],[552,0.014753791110841082],[554,0.010409518512914395],[555,-0.0027837661516584905],[557,0.004250152505553201],[558,0.006220363204763662],[562,0.029749636897977827],[563,-0.004856508284325325],[566,0.02057612947394761],[568,0.011064036907045216],[572,-0.004563324998269853],[577,0.0028593769258906006],[578,0.02135207557358761],[582,-0.018012205437640604],[584,0.02517530149850964],[585,-0.004421473828857127],[587,0.007225751043373753],[589,-0.00402945959459357],[590,0.006787019936516625],[592,-0.003616302074921267],[593,-0.002900874852468165],[596,-0.004052366565721959],[597,-0.003007315578809296],[598,0.0027459370811801827],[599,-0.007236341971000021],[601,-0.002136125571007553],[602,-0.006348140370898295],[606,0.005419793410752147],[608,0.002631297974759063],[611,0.004244024962679064],[612,-0.04889712014341101],[614,0.024729378134773848],[620,-0.013343991700950988],[626,0.0074937964631179325],[628,0.00576563354354513],[631,-0.005340854071014058],[634,-0.005286434000105979],[635,0.023852506762452444],[636,0.002502262901177268],[638,-0.0030961275322798874],[639,-0.009651133046570077],[641,0.005837145921864883],[643,0.19485333172592806],[645,-0.02365589327518136],[646,0.05402911936342095],[649,0.016053543837573146],[654,-0.0067171556781247385],[655,0.003558519880751899],[657,0.16915177253860153],[658,-0.0021312907148484423],[659,0.04969295582615417],[661,0.004078303318669329],[662,-0.003186120262736245],[663,0.004048580727938875],[668,-0.011925948224092382],[669,0.19461239340208208],[671,0.005455305829452566],[672,0.00481505421561824],[673,-0.004486837043663598],[677,0.006469341432134802],[679,0.029713167767566842],[680,-0.01656602649359927],[681,-0.0029242506766752126],[682,0.007288255326655196],[687,-0.0036063928538780324],[692,-0.0045710352495998904],[696,-0.002674450310459974],[697,-0.15904457799804492],[698,-0.010848791054134686],[700,0.0035096370260970836],[706,-0.0031644354650161334],[708,0.0064350235193110054],[712,-0.0066518442596759444],[713,-0.0062163812738000425],[714,0.00392778023837427],[716,0.006176408464846132],[720,0.0034372289186233736],[721,0.005333978375989562],[722,-0.002667892020016406],[723,-0.02826207233967444],[724,0.038170749947635044],[731,-0.0030607723486138303],[732,-0.023683191420081885],[733,0.004300667544656181],[738,-0.005383663980124397],[740,0.0032603406569983963],[741,0.012207167533624368],[742,-0.015801624222134526],[744,0.008762061028603253],[745,0.0029399889557757625],[746,-0.048346292562150485],[747,0.004455199685492106],[749,0.004038899248463125],[753,-0.016001728279506945],[754,-0.0024487502374811758],[755,0.011564772256295645],[757,-0.005436538583341338],[763,-0.005142889479225079],[764,-0.003625805938722684],[767,0.0029823049851796773],[769,-0.0059322656954600645],[775,-0.008981305486244172],[776,0.008820123698881011],[777,-0.004452869897855281],[778,0.00508109135820142],[782,-0.0045446781075179285],[784,-0.005392528142351356],[785,0.0037937837375346217],[786,0.02817931158409869],[787,-0.011913526635457375],[788,0.0037697658172679677],[789,0.0034529857883632145],[790,0.0035572073098202577],[794,-0.0031840871240165023],[797,-0.0037142421634168664],[799,-0.009717801430881504],[800,-0.003806389991587832],[801,0.030847053950367177],[802,-0.010577774821175973],[807,-0.001941048179652356],[809,-0.0031193590400649274],[811,-0.0030347145738674423],[812,0.02772636258692645],[813,0.0025688335749809504],[815,0.004033809634295128],[820,0.003081555161918103],[822,-0.0060163354843302385],[823,0.0019694478752203047],[824,-0.027668718654684663],[825,-0.0028348989195768415],[829,0.004826559454022102],[830,-0.004565263740789876],[832,0.003266991265616893],[833,0.005024977742854625],[835,-0.003976527325636858],[836,0.017578133086618562],[837,0.003835188885836313],[839,-0.005085519387938515],[840,0.005619511942349069],[841,-0.00554610166856573],[843,0.0034373469266002175],[846,0.04128320783044553],[847,0.2583944094948425],[848,0.0025137725912293104],[850,0.006938572232015329],[852,-0.01012811219881396],[853,0.007017471638638405],[854,0.00270706675782235],[857,-0.022507646451259362],[860,-0.0029203203323928642],[861,0.006187218275423286],[863,-0.0051225984438119845],[864,0.0051020838223046275],[865,0.021475582719775885],[868,0.007637660814344141],[874,-0.013241387095292182],[876,0.014942398160950615],[879,0.10125375100853075],[880,-0.004713943484656779],[881,0.05],[883,0.049319001445567286],[884,0.002400805057521264],[885,0.013689290476756169],[887,0.004618742772127241],[890,-0.003641171620820426],[892,-0.005235234822636941],[896,0.11085427898213134],[899,0.0037257153176219],[900,0.01163491525126728],[902,-0.006380192948815805],[903,0.02530058998354478],[904,0.004872842225134972],[905,0.005947998535886589],[906,-0.004526962907654392],[907,0.001981004971266259],[908,-0.0027083099423182246],[911,0.02119017313148045],[912,-0.04190218821417402],[913,0.051697234652315176],[915,-0.0033797475491957633],[916,-0.009216920680422536],[917,0.048423882236133746],[918,-0.002668157146359912],[920,-0.04055994016378425],[925,-0.004780707009624444],[928,0.007177216306847423],[929,-0.002372785027966692],[931,-0.004815317911999894],[932,-0.015064394101083334],[933,0.036257733035043545],[934,0.006711559830053828],[935,0.029880918106005995],[937,-0.039118303039674465],[938,-0.025727701623977993],[939,0.012044680178389383],[943,-0.0026405958064883986],[944,0.0029254359247724714],[945,-0.04263114736925455],[947,0.00436849203686074],[949,0.03161715737136483],[950,0.0028719086525918125],[952,0.0020421084816883255],[953,0.0037839403266326736],[954,0.014439878043377485],[956,-0.004508920578287301],[961,0.025176645483956393],[964,0.008986930180144685],[965,-0.0048305821115456156],[966,-0.04394652542579648],[968,0.0038705967048181774],[970,0.010498991671570082],[971,0.0220430493774582],[972,0.010364167674109043],[973,0.012382137876065897],[974,-0.008915460044029013],[975,0.0035054577472518793],[977,0.0046749734752709205],[978,0.011683812247312752],[979,0.01824129545338142],[980,-0.009152163824656927],[981,-0.006189163719622151],[982,0.005328748928181385],[983,0.004758132446905964],[985,0.005182867661329237],[987,0.016893245647599732],[989,0.02256785699737649],[991,0.0022390150634136897],[992,-0.016622077743617472],[993,-0.0042411698025510165],[994,-0.016901220727566363],[995,0.09766844477384287],[996,-0.002764119444834223],[998,-0.006417935868712535]]}

    with open(dir_path+'/jsonStore/' + str(file_name) + '.json','w') as outfile:
        json.dump(data, outfile)


def sma(data, period):
    j = next(i for i, x in enumerate(data) if x is not None)
    our_range = range(len(data))[j + period - 1:]
    empty_list = [None] * (j + period - 1)
    sub_result = [np.mean(data[i - period + 1: i + 1]) for i in our_range]
    return np.array(empty_list + sub_result)


rate, audio = wavfile.read(dir_path+'/audioFiles/French 79 - Between the Buttons.wav')
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
    #tabInv[i] = sma(tabInv[i], 300)
    tabInv[i] = pd.DataFrame(tabInv[i])
    tabInv[i] = tabInv[i].ewm(span=50).mean()
    tabInv[i] = tabInv[i][0]

dataF = []
for i in range(images):
    tabT = []
    for j in range(len(tabInv)):
        tabT.append(tabInv[j][i])
    dataF.append(tabT)

for i in range(images):
    data = dataF[i][50:178]
    #data = dataF[i]
    #print(data)
    data = 2 * ((data - min(data)) / (max(data) - min(data))) - 1
    with open(dir_path+'/dataFiles/' + str(i) + '.txt', 'w') as f:
        for item in data: f.write("%s\n" % item)
    data = data.tolist()
    new_json(data, str(i))





