#!/bin/bash


mosquitto_pub -h localhost -t "test" -m '{"1":255,"2":255,"3":255,"4":0,"6":0,"7":0,"17":255,"18":0,"19":255,"20":0,"22":0,"23":0,"33":255,"34":255,"35":0,"36":0,"41":255,"42":255,"43":120,"44":0,"45":0}'





mosquitto_pub -h localhost -t "test" -m '{"33":255,"34":255,"35":0,"36":0,"41":255,"42":255,"43":120,"44":0,"45":0}'


#ch41 - focus
#va tenuto 255 che è stretto

# ch 42 - hor
#0 dietro noi
#80 limite pubblico
#170 dietro noi, giro totale 
#250 limite pubblico

#ch 43 - ver
#0 - basso
#120 - alto
#255 - basso












0,0 pubblico basso
