from model import TypingModel

keyboards = list(map(TypingModel.stringToLayout, [
'''
~$0123456789^
`*/{[(=+)]}\%

_HBDRNAQPUF|@
-hbdrnaqpuf&#

YTSMLOEIG:"
ytsmloeig;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_YBMUFAELPQ|@
-ybmufaelpq&#

RGSDHOITN:"
rgsdhoitn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FGDNHOAUBQ|@
-fgdnhoaubq&#

MTSRLYEIP:"
mtsrlyeip;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FGDNLUAYBQ|@
-fgdnluaybq&#

MTSRHOEIP:"
mtsrhoeip;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FGDNROAPUQ|@
-fgdnroapuq&#

MTSHLYEIB:"
mtshlyeib;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FGDNROAPUQ|@
-fgdnroapuq&#

MSTHLYEIB:"
msthlyeib;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FGBNRYAPUQ|@
-fgbnryapuq&#

MTSHLOEID:"
mtshloeid;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FYBNLQAPUG|@
-fybnlqapug&#

MISHROETD:"
mishroetd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FGDNSOAUBQ|@
-fgdnsoaubq&#

MTPHLEYIR:"
mtphleyir;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_QBGLROAPUH|@
-qbglroapuh&#

FTSMNYEID:"
ftsmnyeid;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_YFRUDAELMQ|@
-yfrudaelmq&#

GBSPHOITN:"
gbsphoitn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FGDNHAOUPQ|@
-fgdnhaoupq&#

MSTRLYEIB:"
mstrlyeib;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FGDNHAOIUQ|@
-fgdnhaoiuq&#

MTSRLYEPB:"
mtsrlyepb;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_HBDNROAUFQ|@
-hbdnroaufq&#

MGTSLEYIP:"
mgtsleyip;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FYMUGAILPQ|@
-fymugailpq&#

BRSDHOETN:"
brsdhoetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FHMUPAILBQ|@
-fhmupailbq&#

YRSDGOETN:"
yrsdgoetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FBDNHAYPUQ|@
-fbdnhaypuq&#

MTSRLOEIG:"
mtsrloeig;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_GFRUPAELBQ|@
-gfrupaelbq&#

YMSDHIONT:"
ymsdhiont;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FYBRLEUPMQ|@
-fybrleupmq&#

DISHNAOTG:"
dishnaotg;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FGBNLIAPQY|@
-fgbnliapqy&#

MOSRHUETD:"
mosrhuetd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FGDNLYOUBQ|@
-fgdnlyoubq&#

MTSRHAEIP:"
mtsrhaeip;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_QBGLMYAUPH|@
-qbglmyauph&#

FTSNROEID:"
ftsnroeid;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_HBDRNAQPUF|@
-hbdrnaqpuf&#

YTSMLOEIG:"
ytsmloeig;'

ZXCVWJK<>?
zxcvwjk,.!''',

'''
~$0123456789^
`*/{[(=+)]}\%

_YFRLDTIOBQ|@
-yfrldtiobq&#

GUSNHPMEA:"
gusnhpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_YFRLDTIOBQ|@
-yfrldtiobq&#

GUSNHPMEA:"
gusnhpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FYLRDTIOGQ|@
-fylrdtiogq&#

AMUSNHBPE:"
amusnhbpe;'

ZXCVWJK<>?
zxcvwjk,.!
''',

'''
~$0123456789^
`*/{[(=+)]}\%

_FYLRDTIOGQ|@
-fylrdtiogq&#

BMUSHNPEA:"
bmushnpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.8078
'''
~$0123456789^
`*/{[(=+)]}\%

_BGNMAEDLQY|@
-bgnmaedlqy&#

FISHPUOTR:"
fishpuotr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.8463
'''
~$0123456789^
`*/{[(=+)]}\%

_FGNLAEMPQY|@
-fgnlaempqy&#

BUSRHOITD:"
busrhoitd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.8614
'''
~$0123456789^
`*/{[(=+)]}\%

_BDNLMTIOGQ|@
-bdnlmtiogq&#

YUSRHPFEA:"
yusrhpfea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.8813
'''
~$0123456789^
`*/{[(=+)]}\%

_HLTGAEPBQY|@
-hltgaepbqy&#

FNSDMUOIR:"
fnsdmuoir;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 17.1417
'''
~$0123456789^
`*/{[(=+)]}\%

_YFTBAELPUQ|@
-yftbaelpuq&#

GHSDMOIRN:"
ghsdmoirn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 17.1460
'''
~$0123456789^
`*/{[(=+)]}\%

_YDPBAELHUQ|@
-ydpbaelhuq&#

GMSTFOINR:"
gmstfoinr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 17.3795
'''
~$0123456789^
`*/{[(=+)]}\%

_YSPFIELBUQ|@
-yspfielbuq&#

GMRDHOATN:"
gmrdhoatn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 13.2926
'''
~$0123456789^
`*/{[(=+)]}\%

_YFRLDTIOBQ|@
-yfrldtiobq&#

GUSNHPMEA:"
gusnhpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 13.3237
'''
~$0123456789^
`*/{[(=+)]}\%

_FBRLDTIOGQ|@
-fbrldtiogq&#

YUSNHPMEA:"
yusnhpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 13.8554
'''
~$0123456789^
`*/{[(=+)]}\%

_FDTGOAPBUQ|@
-fdtgoapbuq&#

YHSLMIENR:"
yhslmienr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 13.8563
'''
~$0123456789^
`*/{[(=+)]}\%

_FDLMOAPBUQ|@
-fdlmoapbuq&#

YGSRHIETN:"
ygsrhietn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 13.8623
'''
~$0123456789^
`*/{[(=+)]}\%

_FDNLAEMBUQ|@
-fdnlaembuq&#

YGSHPOITR:"
ygshpoitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 13.9082
'''
~$0123456789^
`*/{[(=+)]}\%

_FDGBAELHUQ|@
-fdgbaelhuq&#

YMSTPOINR:"
ymstpoinr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 14.0823
'''
~$0123456789^
`*/{[(=+)]}\%

_FRTMOAPBGQ|@
-frtmoapbgq&#

YHSLDUEIN:"
yhslduein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.4841
'''
~$0123456789^
`*/{[(=+)]}\%

_UDRHGPIOBQ|@
-udrhgpiobq&#

YFSNLMTEA:"
yfsnlmtea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.4944
'''
~$0123456789^
`*/{[(=+)]}\%

_YPRLGMIUBQ|@
-yprlgmiubq&#

FOSNHDTEA:"
fosnhdtea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.5953
'''
~$0123456789^
`*/{[(=+)]}\%

_FDRMOAPBYQ|@
-fdrmoapbyq&#

GUSLHIETN:"
guslhietn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.6629
'''
~$0123456789^
`*/{[(=+)]}\%

_GMRLUADBYQ|@
-gmrluadbyq&#

FOSNHIETP:"
fosnhietp;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.8608
'''
~$0123456789^
`*/{[(=+)]}\%

_PRTGOALUYQ|@
-prtgoaluyq&#

BHSDMIENF:"
bhsdmienf;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.9128
'''
~$0123456789^
`*/{[(=+)]}\%

_HRTBUAPFYQ|@
-hrtbuapfyq&#

GLSDMOEIN:"
glsdmoein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 17.1731
'''
~$0123456789^
`*/{[(=+)]}\%

_GLDMUIAHYQ|@
-gldmuiahyq&#

FSRTBPEON:"
fsrtbpeon;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.1348
'''
~$0123456789^
`*/{[(=+)]}\%

_FBRLMTIOGQ|@
-fbrlmtiogq&#

YUSNHPDEA:"
yusnhpdea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.1808
'''
~$0123456789^
`*/{[(=+)]}\%

_FMNHTDIOBQ|@
-fmnhtdiobq&#

YUSRLPGEA:"
yusrlpgea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.2794
'''
~$0123456789^
`*/{[(=+)]}\%

_GFNLPMIOBQ|@
-gfnlpmiobq&#

YUSRHDTEA:"
yusrhdtea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.2870
'''
~$0123456789^
`*/{[(=+)]}\%

_YBLRPTOUGQ|@
-yblrptougq&#

FISNHDMEA:"
fisnhdmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.5953
'''
~$0123456789^
`*/{[(=+)]}\%

_GDMNOAPBYQ|@
-gdmnoapbyq&#

FUSLHIETR:"
fuslhietr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.6002
'''
~$0123456789^
`*/{[(=+)]}\%

_FDLMOAPBYQ|@
-fdlmoapbyq&#

GUSHRIETN:"
gushrietn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.6987
'''
~$0123456789^
`*/{[(=+)]}\%

_PSTGOELUYQ|@
-pstgoeluyq&#

BFRDMAINH:"
bfrdmainh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.7013
'''
~$0123456789^
`*/{[(=+)]}\%

_FDMGOAPBUY|@
-fdmgoapbuy&#

QHSTLIENR:"
qhstlienr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.7128
'''
~$0123456789^
`*/{[(=+)]}\%

_FDLMOAPBUY|@
-fdlmoapbuy&#

QGSRHIETN:"
qgsrhietn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.7326
'''
~$0123456789^
`*/{[(=+)]}\%

_FDPLOEMBUY|@
-fdploembuy&#

QGSNHAITR:"
qgsnhaitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.7543
'''
~$0123456789^
`*/{[(=+)]}\%

_HLTGUAPBYQ|@
-hltguapbyq&#

FNSDMOEIR:"
fnsdmoeir;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.8076
'''
~$0123456789^
`*/{[(=+)]}\%

_BLTMUIHPYQ|@
-bltmuihpyq&#

FSRGDAEON:"
fsrgdaeon;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.8399
'''
~$0123456789^
`*/{[(=+)]}\%

_UMGBAELPYQ|@
-umgbaelpyq&#

FHSTDOINR:"
fhstdoinr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 16.8745
'''
~$0123456789^
`*/{[(=+)]}\%

_HBTMOAPFYQ|@
-hbtmoapfyq&#

GRSLDUEIN:"
grslduein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.0756
'''
~$0123456789^
`*/{[(=+)]}\%

_FMRLDTIOBQ|@
-fmrldtiobq&#

YUSNHGPEA:"
yusnhgpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.1125
'''
~$0123456789^
`*/{[(=+)]}\%

_FPRLMTOUBQ|@
-fprlmtoubq&#

YSINHGDEA:"
ysinhgdea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.2358
'''
~$0123456789^
`*/{[(=+)]}\%

_YFNLDTIOBQ|@
-yfnldtiobq&#

HUSRMGPEA:"
husrmgpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.2564
'''
~$0123456789^
`*/{[(=+)]}\%

_FMPGRNIOYQ|@
-fmpgrnioyq&#

BUSTDHLEA:"
bustdhlea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.2656
'''
~$0123456789^
`*/{[(=+)]}\%

_NSDULTIOGQ|@
-nsdultiogq&#

YBRHFPMEA:"
ybrhfpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.4511
'''
~$0123456789^
`*/{[(=+)]}\%

_GDNPAEMLYQ|@
-gdnpaemlyq&#

BUSHFOITR:"
bushfoitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.4652
'''
~$0123456789^
`*/{[(=+)]}\%

_GSNFAEMLYQ|@
-gsnfaemlyq&#

BODHPUITR:"
bodhpuitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5020
'''
~$0123456789^
`*/{[(=+)]}\%

_BPDMAELHYQ|@
-bpdmaelhyq&#

GSITFUONR:"
gsitfuonr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5327
'''
~$0123456789^
`*/{[(=+)]}\%

_FMPGAELHYQ|@
-fmpgaelhyq&#

BUSTDOINR:"
bustdoinr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5489
'''
~$0123456789^
`*/{[(=+)]}\%

_FDMGAELHYQ|@
-fdmgaelhyq&#

BUSTPOINR:"
bustpoinr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5606
'''
~$0123456789^
`*/{[(=+)]}\%

_GDNMOALBYQ|@
-gdnmoalbyq&#

FUSHPIETR:"
fushpietr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5673
'''
~$0123456789^
`*/{[(=+)]}\%

_GFNRAEMPYQ|@
-gfnraempyq&#

BUSLHOITD:"
buslhoitd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5674
'''
~$0123456789^
`*/{[(=+)]}\%

_UPTMOELBYQ|@
-uptmoelbyq&#

GHSDFIANR:"
ghsdfianr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5708
'''
~$0123456789^
`*/{[(=+)]}\%

_FDNLOAGBYQ|@
-fdnloagbyq&#

HUSRMIETP:"
husrmietp;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5716
'''
~$0123456789^
`*/{[(=+)]}\%

_FDRLOAPBYQ|@
-fdrloapbyq&#

GUSMHIETN:"
gusmhietn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5752
'''
~$0123456789^
`*/{[(=+)]}\%

_FPTLOEHBYQ|@
-fptloehbyq&#

GSIDMUANR:"
gsidmuanr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5857
'''
~$0123456789^
`*/{[(=+)]}\%

_FSTPOILUYQ|@
-fstpoiluyq&#

BMRDGAENH:"
bmrdgaenh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5866
'''
~$0123456789^
`*/{[(=+)]}\%

_FMRLOAPUYQ|@
-fmrloapuyq&#

BGSNHIETD:"
bgsnhietd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5921
'''
~$0123456789^
`*/{[(=+)]}\%

_BMUGIALPYQ|@
-bmugialpyq&#

FRSDHOETN:"
frsdhoetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5979
'''
~$0123456789^
`*/{[(=+)]}\%

_FGRMIALPYQ|@
-fgrmialpyq&#

BUSDHOETN:"
busdhoetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6182
'''
~$0123456789^
`*/{[(=+)]}\%

_GSDUIALPYQ|@
-gsduialpyq&#

BMRHFOETN:"
bmrhfoetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6388
'''
~$0123456789^
`*/{[(=+)]}\%

_MPUGAELBYQ|@
-mpugaelbyq&#

FSNDHOITR:"
fsndhoitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6458
'''
~$0123456789^
`*/{[(=+)]}\%

_FRTMOAPBYQ|@
-frtmoapbyq&#

GHSLDUEIN:"
ghslduein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6499
'''
~$0123456789^
`*/{[(=+)]}\%

_LSTFOAPBYQ|@
-lstfoapbyq&#

GHRDMUEIN:"
ghrdmuein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6605
'''
~$0123456789^
`*/{[(=+)]}\%

_GSNPOALUYQ|@
-gsnpoaluyq&#

BMRHFIETD:"
bmrhfietd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7450
'''
~$0123456789^
`*/{[(=+)]}\%

_BFLDOEIHYQ|@
-bfldoeihyq&#

GNSTMUAPR:"
gnstmuapr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7556
'''
~$0123456789^
`*/{[(=+)]}\%

_BMHUAEPLYQ|@
-bmhuaeplyq&#

FSTDGOINR:"
fstdgoinr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7724
'''
~$0123456789^
`*/{[(=+)]}\%

_BLDFIAHPYQ|@
-bldfiahpyq&#

GSRTMUEON:"
gsrtmueon;'

ZXCVWJK<>?
zxcvwjk,.!
''',


# score = 20.0105
'''
~$0123456789^
`*/{[(=+)]}\%

_FRLMDTIOGQ|@
-frlmdtiogq&#

YBSNHUPEA:"
ybsnhupea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.0112
'''
~$0123456789^
`*/{[(=+)]}\%

_FRLMDTIOGQ|@
-frlmdtiogq&#

YBSNHPUEA:"
ybsnhpuea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.0913
'''
~$0123456789^
`*/{[(=+)]}\%

_BFLMDTIOYQ|@
-bflmdtioyq&#

HPSNRGUEA:"
hpsnrguea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1434
'''
~$0123456789^
`*/{[(=+)]}\%

_FDNHPMOUYQ|@
-fdnhpmouyq&#

BSTRLGIEA:"
bstrlgiea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1455
'''
~$0123456789^
`*/{[(=+)]}\%

_FRPGLNIOYQ|@
-frpglnioyq&#

BMSTDUHEA:"
bmstduhea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1902
'''
~$0123456789^
`*/{[(=+)]}\%

_FMDGOALUYQ|@
-fmdgoaluyq&#

BSNTPIERH:"
bsntpierh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1944
'''
~$0123456789^
`*/{[(=+)]}\%

_FMRLOAPUYQ|@
-fmrloapuyq&#

BGSNHIETD:"
bgsnhietd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1966
'''
~$0123456789^
`*/{[(=+)]}\%

_FDNMUAOBYQ|@
-fdnmuaobyq&#

HGSRLIETP:"
hgsrlietp;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1999
'''
~$0123456789^
`*/{[(=+)]}\%

_FRTMUOPBYQ|@
-frtmuopbyq&#

GHSLDAEIN:"
ghsldaein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2050
'''
~$0123456789^
`*/{[(=+)]}\%

_FSPGOILUYQ|@
-fspgoiluyq&#

BMRTDAENH:"
bmrtdaenh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2068
'''
~$0123456789^
`*/{[(=+)]}\%

_FSTMUOPBYQ|@
-fstmuopbyq&#

GHRLDAEIN:"
ghrldaein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2100
'''
~$0123456789^
`*/{[(=+)]}\%

_FSGPOILUYQ|@
-fsgpoiluyq&#

BMRTDAENH:"
bmrtdaenh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2101
'''
~$0123456789^
`*/{[(=+)]}\%

_BPDMOALUYQ|@
-bpdmoaluyq&#

GSNTFIERH:"
gsntfierh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2297
'''
~$0123456789^
`*/{[(=+)]}\%

_BMPFOILUYQ|@
-bmpfoiluyq&#

GRSTDAENH:"
grstdaenh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2529
'''
~$0123456789^
`*/{[(=+)]}\%

_GRNFOAMUYQ|@
-grnfoamuyq&#

BLSHPIETD:"
blshpietd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2712
'''
~$0123456789^
`*/{[(=+)]}\%

_FPLMUAHBYQ|@
-fplmuahbyq&#

GSNTDIEOR:"
gsntdieor;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3083
'''
~$0123456789^
`*/{[(=+)]}\%

_BLDFUAHPYQ|@
-bldfuahpyq&#

GRSTMIEON:"
grstmieon;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3103
'''
~$0123456789^
`*/{[(=+)]}\%

_HFTDUAPBYQ|@
-hftduapbyq&#

GNSLMOEIR:"
gnslmoeir;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3349
'''
~$0123456789^
`*/{[(=+)]}\%

_GMHPOALUYQ|@
-gmhpoaluyq&#

BTSNFIERD:"
btsnfierd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3610
'''
~$0123456789^
`*/{[(=+)]}\%

_GDNMOAUBYQ|@
-gdnmoaubyq&#

FPSLHIETR:"
fpslhietr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.4524
'''
~$0123456789^
`*/{[(=+)]}\%

_FDLMOAUBYQ|@
-fdlmoaubyq&#

GPSRHIETN:"
gpsrhietn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

]))

keyboards = map(TypingModel.stringToLayout, [

# score = 19.6442
'''
~$0123456789^
`*/{[(=+)]}\%

_FMRLDTIOBQ|@
-fmrldtiobq&#

YUSNHGPEA:"
yusnhgpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6473
'''
~$0123456789^
`*/{[(=+)]}\%

_FMRLDTIOBQ|@
-fmrldtiobq&#

YUSNHPGEA:"
yusnhpgea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6545
'''
~$0123456789^
`*/{[(=+)]}\%

_FDNLMTIOBQ|@
-fdnlmtiobq&#

YUSRHGPEA:"
yusrhgpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6701
'''
~$0123456789^
`*/{[(=+)]}\%

_FPRLMTOUBQ|@
-fprlmtoubq&#

YSINHGDEA:"
ysinhgdea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6717
'''
~$0123456789^
`*/{[(=+)]}\%

_FRLMDTIOBQ|@
-frlmdtiobq&#

YUSNHGPEA:"
yusnhgpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6745
'''
~$0123456789^
`*/{[(=+)]}\%

_FDRNMTIOBQ|@
-fdrnmtiobq&#

YUSLHGPEA:"
yuslhgpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6885
'''
~$0123456789^
`*/{[(=+)]}\%

_FBRLDTIOGQ|@
-fbrldtiogq&#

YUSNHPMEA:"
yusnhpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6897
'''
~$0123456789^
`*/{[(=+)]}\%

_FDNLTMIOBQ|@
-fdnltmiobq&#

YUSRHGPEA:"
yusrhgpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6973
'''
~$0123456789^
`*/{[(=+)]}\%

_FBLRDTIOGQ|@
-fblrdtiogq&#

YUSNHPMEA:"
yusnhpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7127
'''
~$0123456789^
`*/{[(=+)]}\%

_GFNLDTIOBQ|@
-gfnldtiobq&#

YUSRHPMEA:"
yusrhpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7403
'''
~$0123456789^
`*/{[(=+)]}\%

_FPRLMDOUBQ|@
-fprlmdoubq&#

YSINHGTEA:"
ysinhgtea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7446
'''
~$0123456789^
`*/{[(=+)]}\%

_YFRLDTIOBQ|@
-yfrldtiobq&#

HUSNMGPEA:"
husnmgpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7480
'''
~$0123456789^
`*/{[(=+)]}\%

_BPLRMTOUGQ|@
-bplrmtougq&#

YISNHDFEA:"
yisnhdfea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7736
'''
~$0123456789^
`*/{[(=+)]}\%

_FMPGRNIOYQ|@
-fmpgrnioyq&#

BUSTDHLEA:"
bustdhlea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.8011
'''
~$0123456789^
`*/{[(=+)]}\%

_NSDULTIOGQ|@
-nsdultiogq&#

YBRHFPMEA:"
ybrhfpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.8151
'''
~$0123456789^
`*/{[(=+)]}\%

_FRLUDTIOGQ|@
-frludtiogq&#

YBSNHPMEA:"
ybsnhpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.8161
'''
~$0123456789^
`*/{[(=+)]}\%

_FRPGLNIOYQ|@
-frpglnioyq&#

BUSTDMHEA:"
bustdmhea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.8396
'''
~$0123456789^
`*/{[(=+)]}\%

_YFLMDTIOGQ|@
-yflmdtiogq&#

HUSNRBPEA:"
husnrbpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.9796
'''
~$0123456789^
`*/{[(=+)]}\%

_FSLRDTIOGQ|@
-fslrdtiogq&#

YBUHNPMEA:"
ybuhnpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.0647
'''
~$0123456789^
`*/{[(=+)]}\%

_GSNFAEMLYQ|@
-gsnfaemlyq&#

BODHPUITR:"
bodhpuitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.0728
'''
~$0123456789^
`*/{[(=+)]}\%

_GDNPAEMLYQ|@
-gdnpaemlyq&#

BUSHFOITR:"
bushfoitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.0912
'''
~$0123456789^
`*/{[(=+)]}\%

_BPDMOELHYQ|@
-bpdmoelhyq&#

GSITFUANR:"
gsitfuanr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1090
'''
~$0123456789^
`*/{[(=+)]}\%

_NRDGTMEABQ|@
-nrdgtmeabq&#

YLSUHPFIO:"
ylsuhpfio;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1113
'''
~$0123456789^
`*/{[(=+)]}\%

_FRNBLTIOQG|@
-frnbltioqg&#

YPSHUDMEA:"
ypshudmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1122
'''
~$0123456789^
`*/{[(=+)]}\%

_DLNUMTEABQ|@
-dlnumteabq&#

YSRHPGFIO:"
ysrhpgfio;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1361
'''
~$0123456789^
`*/{[(=+)]}\%

_GSNMUALBYQ|@
-gsnmualbyq&#

FODPHIETR:"
fodphietr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1361
'''
~$0123456789^
`*/{[(=+)]}\%

_GSNPUALBYQ|@
-gsnpualbyq&#

FODHMIETR:"
fodhmietr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1392
'''
~$0123456789^
`*/{[(=+)]}\%

_LSUMTFIOBQ|@
-lsumtfiobq&#

YGRHNPDEA:"
ygrhnpdea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1447
'''
~$0123456789^
`*/{[(=+)]}\%

_FMPGAELHYQ|@
-fmpgaelhyq&#

BUSTDOINR:"
bustdoinr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1476
'''
~$0123456789^
`*/{[(=+)]}\%

_FDMGAELHYQ|@
-fdmgaelhyq&#

BUSTPOINR:"
bustpoinr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1532
'''
~$0123456789^
`*/{[(=+)]}\%

_GDNMOALBYQ|@
-gdnmoalbyq&#

FUSHPIETR:"
fushpietr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1553
'''
~$0123456789^
`*/{[(=+)]}\%

_GDNMUALBYQ|@
-gdnmualbyq&#

FOSHPIETR:"
foshpietr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1572
'''
~$0123456789^
`*/{[(=+)]}\%

_FPLDUEHBYQ|@
-fplduehbyq&#

GSITMOANR:"
gsitmoanr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1641
'''
~$0123456789^
`*/{[(=+)]}\%

_UPTMOALBYQ|@
-uptmoalbyq&#

GHSDFIENR:"
ghsdfienr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1689
'''
~$0123456789^
`*/{[(=+)]}\%

_FDNLOAGBYQ|@
-fdnloagbyq&#

HUSRMIETP:"
husrmietp;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1694
'''
~$0123456789^
`*/{[(=+)]}\%

_FDRLOAPBYQ|@
-fdrloapbyq&#

GUSMHIETN:"
gusmhietn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1707
'''
~$0123456789^
`*/{[(=+)]}\%

_FMPGIELHYQ|@
-fmpgielhyq&#

BUSTDAONR:"
bustdaonr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1777
'''
~$0123456789^
`*/{[(=+)]}\%

_FDNLUAOBYQ|@
-fdnluaobyq&#

HGSRMIETP:"
hgsrmietp;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1821
'''
~$0123456789^
`*/{[(=+)]}\%

_FSTPOILUYQ|@
-fstpoiluyq&#

BMRDGAENH:"
bmrdgaenh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1863
'''
~$0123456789^
`*/{[(=+)]}\%

_BMUGIALPYQ|@
-bmugialpyq&#

FRSDHOETN:"
frsdhoetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1882
'''
~$0123456789^
`*/{[(=+)]}\%

_HDTGAELPYQ|@
-hdtgaelpyq&#

BUSFMOIRN:"
busfmoirn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1883
'''
~$0123456789^
`*/{[(=+)]}\%

_FSTGOILUYQ|@
-fstgoiluyq&#

BMRDPAENH:"
bmrdpaenh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1889
'''
~$0123456789^
`*/{[(=+)]}\%

_FGRMIALPYQ|@
-fgrmialpyq&#

BUSDHOETN:"
busdhoetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1902
'''
~$0123456789^
`*/{[(=+)]}\%

_FMDGOALUYQ|@
-fmdgoaluyq&#

BSNTPIERH:"
bsntpierh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1903
'''
~$0123456789^
`*/{[(=+)]}\%

_FGNLAEMPYQ|@
-fgnlaempyq&#

BUSRHOITD:"
busrhoitd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1942
'''
~$0123456789^
`*/{[(=+)]}\%

_UMTPOELBYQ|@
-umtpoelbyq&#

GHSDFIANR:"
ghsdfianr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1944
'''
~$0123456789^
`*/{[(=+)]}\%

_FMRLOAPUYQ|@
-fmrloapuyq&#

BGSNHIETD:"
bgsnhietd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1973
'''
~$0123456789^
`*/{[(=+)]}\%

_FRTMOAPBYQ|@
-frtmoapbyq&#

GHSLDUEIN:"
ghslduein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1989
'''
~$0123456789^
`*/{[(=+)]}\%

_LSTFOAPBYQ|@
-lstfoapbyq&#

GHRDMUEIN:"
ghrdmuein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.1999
'''
~$0123456789^
`*/{[(=+)]}\%

_FRTMUOPBYQ|@
-frtmuopbyq&#

GHSLDAEIN:"
ghsldaein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2015
'''
~$0123456789^
`*/{[(=+)]}\%

_LSTFUOPBYQ|@
-lstfuopbyq&#

GHRDMAEIN:"
ghrdmaein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2050
'''
~$0123456789^
`*/{[(=+)]}\%

_FSPGOILUYQ|@
-fspgoiluyq&#

BMRTDAENH:"
bmrtdaenh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2101
'''
~$0123456789^
`*/{[(=+)]}\%

_BPDMOALUYQ|@
-bpdmoaluyq&#

GSNTFIERH:"
gsntfierh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2124
'''
~$0123456789^
`*/{[(=+)]}\%

_GSDUIALPYQ|@
-gsduialpyq&#

BMRHFOETN:"
bmrhfoetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2145
'''
~$0123456789^
`*/{[(=+)]}\%

_GSPUIALBYQ|@
-gspuialbyq&#

FMRDHOETN:"
fmrdhoetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2191
'''
~$0123456789^
`*/{[(=+)]}\%

_FRTMOAPBQY|@
-frtmoapbqy&#

GHSLDUEIN:"
ghslduein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2297
'''
~$0123456789^
`*/{[(=+)]}\%

_BMPFOILUYQ|@
-bmpfoiluyq&#

GRSTDAENH:"
grstdaenh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2484
'''
~$0123456789^
`*/{[(=+)]}\%

_MPUGAELBYQ|@
-mpugaelbyq&#

FSNDHOITR:"
fsndhoitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2487
'''
~$0123456789^
`*/{[(=+)]}\%

_PSTMOILUYQ|@
-pstmoiluyq&#

BFRDGAENH:"
bfrdgaenh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2509
'''
~$0123456789^
`*/{[(=+)]}\%

_GRNPOAMUYQ|@
-grnpoamuyq&#

BLSHFIETD:"
blshfietd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2599
'''
~$0123456789^
`*/{[(=+)]}\%

_HSTGUOPBYQ|@
-hstguopbyq&#

FLRDMAEIN:"
flrdmaein;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2664
'''
~$0123456789^
`*/{[(=+)]}\%

_FPLDUAHBYQ|@
-fplduahbyq&#

GSNTMIEOR:"
gsntmieor;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2703
'''
~$0123456789^
`*/{[(=+)]}\%

_FSTGOALUYQ|@
-fstgoaluyq&#

BPRDMIENH:"
bprdmienh;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2746
'''
~$0123456789^
`*/{[(=+)]}\%

_FDRNAILPYQ|@
-fdrnailpyq&#

BUSMHOETG:"
busmhoetg;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2813
'''
~$0123456789^
`*/{[(=+)]}\%

_GMNHOALUYQ|@
-gmnhoaluyq&#

BTSPFIERD:"
btspfierd;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.2890
'''
~$0123456789^
`*/{[(=+)]}\%

_FDNLAEMBUY|@
-fdnlaembuy&#

QGSHPOITR:"
qgshpoitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3025
'''
~$0123456789^
`*/{[(=+)]}\%

_BGNMAEDLYQ|@
-bgnmaedlyq&#

FISHPUOTR:"
fishpuotr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3083
'''
~$0123456789^
`*/{[(=+)]}\%

_BLDFUAHPYQ|@
-bldfuahpyq&#

GRSTMIEON:"
grstmieon;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3094
'''
~$0123456789^
`*/{[(=+)]}\%

_FPLMAEDBUY|@
-fplmaedbuy&#

QGSNHOITR:"
qgsnhoitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3103
'''
~$0123456789^
`*/{[(=+)]}\%

_HFTDUAPBYQ|@
-hftduapbyq&#

GNSLMOEIR:"
gnslmoeir;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3121
'''
~$0123456789^
`*/{[(=+)]}\%

_BLFMUAHPYQ|@
-blfmuahpyq&#

GRSTDIEON:"
grstdieon;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3141
'''
~$0123456789^
`*/{[(=+)]}\%

_FDTGOAPBUY|@
-fdtgoapbuy&#

QHSLMIENR:"
qhslmienr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3149
'''
~$0123456789^
`*/{[(=+)]}\%

_BFLDOAIHYQ|@
-bfldoaihyq&#

GNSTMUEPR:"
gnstmuepr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3182
'''
~$0123456789^
`*/{[(=+)]}\%

_BLDFUIHPYQ|@
-bldfuihpyq&#

GSRTMAEON:"
gsrtmaeon;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3358
'''
~$0123456789^
`*/{[(=+)]}\%

_BFDLAEPHYQ|@
-bfdlaephyq&#

GISTMUONR:"
gistmuonr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3366
'''
~$0123456789^
`*/{[(=+)]}\%

_DGFNAOMLYQ|@
-dgfnaomlyq&#

BSIHPUETR:"
bsihpuetr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3408
'''
~$0123456789^
`*/{[(=+)]}\%

_FDRLOAPBUY|@
-fdrloapbuy&#

QGSMHIETN:"
qgsmhietn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3466
'''
~$0123456789^
`*/{[(=+)]}\%

_UFMRTLEOBQ|@
-ufmrtleobq&#

YDSHNGPIA:"
ydshngpia;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3478
'''
~$0123456789^
`*/{[(=+)]}\%

_FRDLHAEPYQ|@
-frdlhaepyq&#

GNSMTUOIB:"
gnsmtuoib;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3496
'''
~$0123456789^
`*/{[(=+)]}\%

_FDLROAPBUY|@
-fdlroapbuy&#

QGSMHIETN:"
qgsmhietn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3579
'''
~$0123456789^
`*/{[(=+)]}\%

_DGFNUOIBYQ|@
-dgfnuoibyq&#

HSTMLAERP:"
hstmlaerp;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3600
'''
~$0123456789^
`*/{[(=+)]}\%

_BMUGAEPLYQ|@
-bmugaeplyq&#

FNSDHOITR:"
fnsdhoitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3614
'''
~$0123456789^
`*/{[(=+)]}\%

_FDGBAELHUY|@
-fdgbaelhuy&#

QMSTPOINR:"
qmstpoinr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3730
'''
~$0123456789^
`*/{[(=+)]}\%

_FMHLIADGQY|@
-fmhliadgqy&#

BUSNROETP:"
busnroetp;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3780
'''
~$0123456789^
`*/{[(=+)]}\%

_MRFUIAPBYQ|@
-mrfuiapbyq&#

HLSDGOETN:"
hlsdgoetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.3851
'''
~$0123456789^
`*/{[(=+)]}\%

_DFRLOEBPQY|@
-dfrloebpqy&#

GUSMHAITN:"
gusmhaitn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.4190
'''
~$0123456789^
`*/{[(=+)]}\%

_PMHUIALBYQ|@
-pmhuialbyq&#

FGSDROETN:"
fgsdroetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.4512
'''
~$0123456789^
`*/{[(=+)]}\%

_FDRNUABPYQ|@
-fdrnuabpyq&#

HTSMLOEIG:"
htsmloeig;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.4530
'''
~$0123456789^
`*/{[(=+)]}\%

_DGNHOAIFYQ|@
-dgnhoaifyq&#

MSTRLUEPB:"
mstrluepb;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.4769
'''
~$0123456789^
`*/{[(=+)]}\%

_BPHLMGIOYQ|@
-bphlmgioyq&#

FTSNRUDEA:"
ftsnrudea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.4786
'''
~$0123456789^
`*/{[(=+)]}\%

_FDMLAOBPYQ|@
-fdmlaobpyq&#

HGSRNUEIT:"
hgsrnueit;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.4922
'''
~$0123456789^
`*/{[(=+)]}\%

_SYRNDTIABQ|@
-syrndtiabq&#

MFUHLPGEO:"
mfuhlpgeo;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.4961
'''
~$0123456789^
`*/{[(=+)]}\%

_FBHNMTAUGQ|@
-fbhnmtaugq&#

YOSRLDPEI:"
yosrldpei;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.5852
'''
~$0123456789^
`*/{[(=+)]}\%

_GSFUEAMLYQ|@
-gsfueamlyq&#

BDRPHIOTN:"
bdrphiotn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.7682
'''
~$0123456789^
`*/{[(=+)]}\%

_GSMROIFPYQ|@
-gsmroifpyq&#

LUBHDAETN:"
lubhdaetn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.8566
'''
~$0123456789^
`*/{[(=+)]}\%

_HBDGEALMUY|@
-hbdgealmuy&#

QRSPFOITN:"
qrspfoitn;'

ZXCVWJK<>?
zxcvwjk,.!
''',

])

keyboards = map(TypingModel.stringToLayout, [

# score = 19.3462
'''
~$0123456789^
`*/{[(=+)]}\%

_BPNLMTOUGQ|@
-bpnlmtougq&#

:SIRHFDEA"Y
;sirhfdea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.3472
'''
~$0123456789^
`*/{[(=+)]}\%

_BPNLMTOUGQ|@
-bpnlmtougq&#

:SIRHFDEA"Y
;sirhfdea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.3493
'''
~$0123456789^
`*/{[(=+)]}\%

_BPRLMTOUGQ|@
-bprlmtougq&#

:SINHFDEAY"
;sinhfdeay'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.4640
'''
~$0123456789^
`*/{[(=+)]}\%

_FBRLDTIOGQ|@
-fbrldtiogq&#

:USNHPMEA"Y
;usnhpmea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.4641
'''
~$0123456789^
`*/{[(=+)]}\%

_FBRLDTIOGQ|@
-fbrldtiogq&#

:USNHMPEAY"
;usnhmpeay'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.4654
'''
~$0123456789^
`*/{[(=+)]}\%

_FBRLDTIOGQ|@
-fbrldtiogq&#

:USNHPMEA"Y
;usnhpmea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.4654
'''
~$0123456789^
`*/{[(=+)]}\%

_FBRLDTIOGQ|@
-fbrldtiogq&#

:USNHPMEAY"
;usnhpmeay'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.4736
'''
~$0123456789^
`*/{[(=+)]}\%

_FPRLDTIOGQ|@
-fprldtiogq&#

:USNHBMEAY"
;usnhbmeay'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.4756
'''
~$0123456789^
`*/{[(=+)]}\%

_FBLRDTIOGQ|@
-fblrdtiogq&#

:USNHPMEA"Y
;usnhpmea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.4792
'''
~$0123456789^
`*/{[(=+)]}\%

_FBRLMTIOGQ|@
-fbrlmtiogq&#

:USNHDPEAY"
;usnhdpeay'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.4824
'''
~$0123456789^
`*/{[(=+)]}\%

_FPLRDTIOGQ|@
-fplrdtiogq&#

:USNHBMEA"Y
;usnhbmea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.5110
'''
~$0123456789^
`*/{[(=+)]}\%

_FPRLMTIOBQ|@
-fprlmtiobq&#

:USNHGDEA"Y
;usnhgdea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6455
'''
~$0123456789^
`*/{[(=+)]}\%

_PSLUDTIOGQ|@
-psludtiogq&#

:BRNHFMEA"Y
;brnhfmea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.6977
'''
~$0123456789^
`*/{[(=+)]}\%

_HFRMDTIOBQ|@
-hfrmdtiobq&#

:USNLGPEA"Y
;usnlgpea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7418
'''
~$0123456789^
`*/{[(=+)]}\%

_YFRLDTIOBQ|@
-yfrldtiobq&#

HUSNMGPEA:"
husnmgpea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7489
'''
~$0123456789^
`*/{[(=+)]}\%

_FMPGRNIO:Q|@
-fmpgrnio;q&#

BUSTDHLEAY"
bustdhleay'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7688
'''
~$0123456789^
`*/{[(=+)]}\%

_FSTPLNIO:Q|@
-fstplnio;q&#

BURDGHMEAY"
burdghmeay'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 19.7982
'''
~$0123456789^
`*/{[(=+)]}\%

_NSDULTIOGQ|@
-nsdultiogq&#

YBRHFPMEA:"
ybrhfpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 20.0640
'''
~$0123456789^
`*/{[(=+)]}\%

_GSNFAEMLYQ|@
-gsnfaemlyq&#

BODHPUITR:"
bodhpuitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

])


keyboards = map(TypingModel.stringToLayout, [

# score = 22.1467
'''
~$0123456789^
`*/{[(=+)]}\%

_BPNLMTOUGQ|@
-bpnlmtougq&#

:SIRHFDEA"Y
;sirhfdea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 22.2782
'''
~$0123456789^
`*/{[(=+)]}\%

_FBRLDTIOGQ|@
-fbrldtiogq&#

:USNHPMEA"Y
;usnhpmea'y

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 22.4658
'''
~$0123456789^
`*/{[(=+)]}\%

_FDGBRNIOMQ|@
-fdgbrniomq&#

YUSTPHLEA:"
yustphlea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 22.5432
'''
~$0123456789^
`*/{[(=+)]}\%

_FSTPLNIOYQ|@
-fstplnioyq&#

BURDGHMEA:"
burdghmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 22.6569
'''
~$0123456789^
`*/{[(=+)]}\%

_NSDULTIOGQ|@
-nsdultiogq&#

YBRHFPMEA:"
ybrhfpmea;'

ZXCVWJK<>?
zxcvwjk,.!
''',

# score = 22.9560
'''
~$0123456789^
`*/{[(=+)]}\%

_GSNFAEMLYQ|@
-gsnfaemlyq&#

BODHPUITR:"
bodhpuitr;'

ZXCVWJK<>?
zxcvwjk,.!
''',

])
