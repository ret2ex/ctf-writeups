from Crypto.Util.number import *

p = 2715012803
q = 1303040714225236316914247837592023713767455507463490984564764762906695038672913859186489193574070334540706541230951
r = 122292395736421852773703087479073197467899993060671630547432160599400345642934010526544671364817
s = 73038144973268535275920197472661886117932030510423949891205041038353924830738251238127
e = 65537
n = 31599415905194296507531163994468257280886159280045654346389430217405819290199334738577568528414824952061262558727052291045816515870348057534996441596560396962516719727878569643953152119895297353348080193869479088114850667155373326828408666807238584625432868509009967976378084883283066242914464294233411627
c = 11371525982887248215036029303506383319725323173791816242922348267059091038845164126422411329763551336318264887183213679689757761368186436315189029720350805092964515239812759488055450797557376437081404871060787004042110689348646779529227539692241991396962852995556540999064671425810298104591755058349120054

phi = (p-1)*(q-1)*(r-1)*(s-1)
d = inverse(e,phi)
print(long_to_bytes(pow(c,d,n)))
