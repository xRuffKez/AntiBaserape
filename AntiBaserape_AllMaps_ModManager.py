import bf2
import host
import mm_utils
from bf2.stats.constants import *
from bf2 import g_debug
import math
import time


# Set the version of your module here
__version__ = 1.5

# Set the required module versions here
__required_modules__ = {
'modmanager': 1.0
}

# Does this module support reload ( are all its reference closed on shutdown? )
__supports_reload__ = False

# Set the description of your module here
__description__ = "AntiBaseRape 2 v%s" % __version__


class fStt(object):
   def __init__(self, player):
   	self.timedeath = 0
   	self.warning = 0
self.enterVeh = 0

class new_baserape_maps(object):
   def __init__(self, map, num_cp, army):
if map == "daqing_oilfields":
    if army == 1:
	self.tch_x = [ {'x':-246, 'y':380.5, 'z':165, 'h':25, 'r':85}, {'x':-110, 'y':533, 'z':155, 'h':18, 'r':90} ]		# PLA(NB, VPP)
	    else:
	self.tch_x = [ {'x':346, 'y':-578, 'z':120, 'h':38, 'r':150} ]								# USA(NB)
if map == "dalian_plant":
    if army == 1:
	self.tch_x = [ {'x':-707, 'y':-367, 'z':180, 'h':25, 'r':115}, {'x':-796, 'y':-125.5, 'z':180, 'h':25, 'r':30} ]	# PLA(NB, VPP)
	    else:
	self.tch_x = [ {'x':763, 'y':-13, 'z':155, 'h':35, 'r':50} ]								# USA(NB)
if map == "gulf_of_oman":
    if army == 1:
	self.tch_x = [ {'x':310, 'y':240, 'z':24, 'h':25, 'r':50}, {'x':127.5, 'y':250, 'z':23, 'h':25, 'r':40} ]		# MEC(NB, heli)
	    else:
	self.tch_x = [ {'x':-677, 'y':-490, 'z':38, 'h':35, 'r':60} ]								# USA(NB)
if map == "operation_clean_sweep":
    if army == 1:
	self.tch_x = [ {'x':-121, 'y':-555, 'z':31, 'h':8, 'r':16, 'point':'smallairstrip', 'owner':1, 'c':13}, {'x':703.5, 'y':83, 'z':29, 'h':15, 'r':25, 'point':'mecairfield', 'owner':1, 'c':13}, {'x':256.3, 'y':-397.8, 'z':37, 'h':15, 'r':9, 'point':'communicationcentral', 'owner':1, 'c':13} ]		# MEC(VPP, VPP(base), heli)
	    else:
	self.tch_x = [ {'x':-552, 'y':544, 'z':29, 'h':15, 'r':50}, {'x':-428, 'y':667.5, 'z':36, 'h':20, 'r':48}, {'x':-328, 'y':682, 'z':36, 'h':25, 'r':50} ] # USA(NB, VPP, VPP)
if map == "kubra_dam":
    if army == 1:
	self.tch_x = [ {'x':-496.5, 'y':-730, 'z':66, 'h':10, 'r':40, 'point':'intake', 'owner':1, 'c':13}, {'x':-458.5, 'y':-584, 'z':65, 'h':25, 'r':25, 'point':'intake', 'owner':1, 'c':13} ]		# MEC(VPP, heli)
	    else:
	self.tch_x = [ {'x':158.5, 'y':125.5, 'z':60, 'h':20, 'r':65}, {'x':519, 'y':332.5, 'z':75, 'h':30, 'r':85} ]		# USA(NB, VPP)
if map == "wake_island_2007":
    if army == 1:
	self.tch_x = [ {'x':408, 'y':-374, 'z':100, 'h':10, 'r':15, 'point':'airfield', 'owner':1, 'c':9}, {'x':373, 'y':-350, 'z':100, 'h':15, 'r':15, 'point':'airfield', 'owner':1, 'c':9} ]		# PLA(VPP, heli)
	    else:
	self.tch_x = [ {'x':-745.5, 'y':633.5, 'z':98, 'h':30, 'r':55} ]							# USA(NB)
if map == "zatar_wetlands":
    if army == 1:
	self.tch_x = [ {'x':727, 'y':-401, 'z':60, 'h':17, 'r':75}, {'x':795, 'y':-510, 'z':60, 'h':25, 'r':45} ]		# MEC(NB, VPP)
	    else:
	if num_cp == 7:
	    self.tch_x = [ {'x':-772, 'y':102, 'z':41, 'h':20, 'r':80}, {'x':-849, 'y':153.5, 'z':38, 'h':25, 'r':40} ]		# USA(NB, NB(VPP))
	else:
	    self.tch_x = [ {'x':-386, 'y':921, 'z':48, 'h':25, 'r':60}, {'x':-565, 'y':482, 'z':30, 'h':15, 'r':85} ]		# USA(NB(VPP), NB)
if map == "fushe_pass":
    if army == 1:
	if num_cp == 6:
	    self.tch_x = [ {'x':-531.5, 'y':231.7, 'z':90, 'h':30, 'r':70} ]							# PLA(NB)
	else:
	    self.tch_x = [ {'x':-668, 'y':-493.8, 'z':115, 'h':40, 'r':130} ]							# PLA(NB)
	    else:
	if num_cp == 6:
	    self.tch_x = [ {'x':302, 'y':-203, 'z':80, 'h':30, 'r':60} ]							# USA(NB)
	else:
	    self.tch_x = [ {'x':608.5, 'y':576.8, 'z':85, 'h':25, 'r':80}, {'x':734.5, 'y':712, 'z':87, 'h':35, 'r':65} ]	# USA(NB, VPP)
if map == "dragon_valley":
    if army == 1:
	if num_cp == 6:
	    self.tch_x = [ {'x':92.5, 'y':-679, 'z':100, 'h':25, 'r':30, 'point':'refinery', 'owner':1, 'c':13} ]		# PLA(Heli)
	else:
	    self.tch_x = [ {'x':92.5, 'y':-679, 'z':100, 'h':25, 'r':30, 'point':'refinery', 'owner':1, 'c':13}, {'x':185.5, 'y':-647, 'z':100, 'h':20, 'r':35, 'point':'refinery', 'owner':1, 'c':13} ]	# PLA(Heli, VPP)
	    else:
	if num_cp == 6:
	    self.tch_x = [ {'x':116, 'y':314, 'z':51, 'h':25, 'r':40} ]								# USA(NB)
	else:
	    self.tch_x = [ {'x':338.5, 'y':846, 'z':67, 'h':30, 'r':55} ]							# USA(NB)
if map == "highway_tampa":
    if army == 1:
	self.tch_x = [ {'x':-493, 'y':636.5, 'z':25, 'h':25, 'r':105} ]								# MEC(NB)
	    else:
	self.tch_x = [ {'x':608, 'y':-526, 'z':25, 'h':15, 'r':50},{'x':706, 'y':-466.5, 'z':26, 'h':25, 'r':50} ]		# USA(NB, VPP)
if map == "taraba_quarry":
    if army == 1:
	if num_cp == 5:
	    self.tch_x = [ {'x':18.5, 'y':186.4, 'z':120, 'h':25, 'r':35} ]							# MEC(NB)
	else:
	    self.tch_x = [ {'x':-489, 'y':-553, 'z':155, 'h':25, 'r':70}, {'x':-645.5, 'y':-525, 'z':160, 'h':20, 'r':50} ]	# MEC(NB, VPP)
 	    else:
	if num_cp == 7:
	    self.tch_x = [ {'x':427, 'y':-461.5, 'z':155, 'h':20, 'r':60}, {'x':575.5, 'y':-420, 'z':160, 'h':20, 'r':45} ]	# EURO(NB, VPP)
if map == "operationsmokescreen":
    if army == 1:
	self.tch_x = [ {'x':72.5, 'y':-522, 'z':96, 'h':15, 'r':60}, {'x':108, 'y':-629, 'z':87, 'h':30, 'r':70} ]		# MEC(NB, VPP)
	    else:
	self.tch_x = [ {'x':7, 'y':430.5, 'z':96, 'h':15, 'r':55}, {'x':87, 'y':528.5, 'z':97, 'h':30, 'r':80} ]		# EURO(NB, VPP)
if map == "road_to_jalalabad":
    if army == 2:
	self.tch_x = [ {'x':-205.4, 'y':7.7, 'z':40, 'h':15, 'r':45} ]								# USA(NB)
if map == "sharqi_peninsula":
    if army == 1:
	if num_cp == 4:
	    self.tch_x = [ {'x':-316.3, 'y':-226.2, 'z':78, 'h':6, 'r':25} ]							# MEC(NB)
	else:
	    self.tch_x = [ {'x':-647, 'y':205, 'z':90, 'h':15, 'r':27}, {'x':-605, 'y':-201, 'z':90, 'h':15, 'r':35}, {'x':-288.5, 'y':-597, 'z':70, 'h':15, 'r':25}, {'x':-247.5, 'y':-585, 'z':75, 'h':20, 'r':18} ]	# MEC(NB, NB, NB, Heli)
    else:
	if num_cp > 4:
	    self.tch_x = [ {'x':-98.25, 'y':-144.25, 'z':128, 'h':15, 'r':15, 'point':'tvstation', 'owner':2, 'c':13} ]		# USA(Heli)
if map == "strike_at_karkand":
    if army == 2:
	self.tch_x = [ {'x':-160, 'y':-282, 'z':159, 'h':10, 'r':40} ]								# USA(NB)
if map == "operation_blue_pearl":
    if num_cp > 4:
	if army == 2:
	    self.tch_x = [ {'x':282, 'y':-123, 'z':15, 'h':20, 'r':58} ]							# USA(island)
if map == "midnight_sun":
    if num_cp > 4:
	if army == 2:
	    self.tch_x = [ {'x':533, 'y':-40, 'z':110, 'h':25, 'r':65}, {'x':607, 'y':61, 'z':110, 'h':25, 'r':75} ]		# USA()
	else:
	    self.tch_x = [ {'x':-735, 'y':-382, 'z':96, 'h':20, 'r':75}, {'x':-664, 'y':-346, 'z':103, 'h':20, 'r':82} ]	# PLA()
if map == "operationharvest":
    if army == 2:
	if num_cp == 5:
	    self.tch_x = [ {'x':471.7, 'y':436, 'z':30, 'h':20, 'r':59} ]							# USA(NB)
	if num_cp == 8:
	    self.tch_x = [ {'x':-405, 'y':-561, 'z':32, 'h':25, 'r':47}, {'x':-455, 'y':-495, 'z':28, 'h':25, 'r':51} ]	# USA(NB, heli)
	if num_cp == 9:
	    self.tch_x = [ {'x':-405, 'y':-561, 'z':32, 'h':25, 'r':47}, {'x':-442, 'y':-483, 'z':28, 'h':25, 'r':42}, {'x':340, 'y':-486, 'z':48, 'h':25, 'r':31} ] # USA(NB, heli)
    else:
	if num_cp == 8:
	    self.tch_x = [ {'x':245, 'y':678, 'z':35, 'h':25, 'r':42}, {'x':215, 'y':560, 'z':28, 'h':25, 'r':48} ]		# MEC(heli,NB)
	if num_cp == 9:
	    self.tch_x = [ {'x':245, 'y':678, 'z':35, 'h':25, 'r':42} ]								# MEC(heli)
if map == "operationroadrage":
    if army == 2:
	if num_cp == 5:
	    self.tch_x = [ {'x':329, 'y':127.5, 'z':50, 'h':15, 'r':57} ]							# USA()
	if num_cp == 7:
	    self.tch_x = [ {'x':-130, 'y':818, 'z':50, 'h':20, 'r':47}, {'x':45, 'y':808, 'z':45, 'h':20, 'r':35} ]		# USA()
    else:
	if num_cp == 5:
	    self.tch_x = [ {'x':-169, 'y':-188, 'z':40, 'h':20, 'r':62} ]							# MEC()	    
	if num_cp == 7:
	    self.tch_x = [ {'x':32, 'y':-738, 'z':45, 'h':20, 'r':67}, {'x':-148.5, 'y':-738, 'z':45, 'h':20, 'r':43} ]		# MEC(heli,NB)

class old_baserape_maps(object):
   def __init__(self, map, army):
self.r = 0
if map == "greatwall" and army==1:
    self.r = 50
if map == "greatwall" and army==2:
    self.r = 30
if map == "jibbel_city" and army==2:
    self.r = 30
if map == "bocage_2005" and army==1:
    self.r = 65
if map == "bocage_2005" and army==2:
    self.r = 40
if map == "strike_at_karkand_2" and army==2:
    self.r = 40
if map == "berlin" and army==2:
    self.r = 18
if map == "heliwar" and army==2:
    self.r = 125
if map == "heliwar" and army==1:
    self.r = 115
if map == "rising_city" and army==2:
    self.r = 30
if map == "vulcan_island" and army==2:
    self.r = 35


check_new_maps = { "daqing_oilfields":[7,9], "gulf_of_oman":[7,9], "dalian_plant":[6,8], "operation_clean_sweep":[4,6,8], "kubra_dam":[8,9], 
    "wake_island_2007":[6],"zatar_wetlands":[7,9],"dragon_valley":[6,11],"fushe_pass":[6,10],"highway_tampa":[6,8],"taraba_quarry":[5,7],
    "operationsmokescreen":[7],"road_to_jalalabad":[7,8],"sharqi_peninsula":[4,8,9], "strike_at_karkand":[7,9],"operation_blue_pearl":[7,8],
    "midnight_sun":[6,8],"operationharvest":[5,8,9],"operationroadrage":[5,7]
    }

check_old_maps = ["greatwall","jibbel_city","stream","bocage_2005","strike_at_karkand_2","berlin","cp_abadan","vulcan_island","rising_city", "heliwar"]

check_noVeh_maps = ["greatwall","sharqi_peninsula","road_to_jalalabad","jibbel_city","berlin"]

mapName = ""
noVehicles = 0
num_cp = 0


class new_baserape2( object ):
def __init__( self, modManager ):
    self.mm = modManager
    self.__state = 0

       def onEnterVehicle( self, player, vehicle, freeSoldier):
    plVehicle = player.getVehicle()
    pl_Vehicle = bf2.objectManager.getRootParent(plVehicle)
   	    if ((getVehicleType(pl_Vehicle.templateName) == VEHICLE_TYPE_HELICOPTER) or (getVehicleType(pl_Vehicle.templateName) == VEHICLE_TYPE_AVIATOR)):
   		player.faa.enterVeh = int(time.time())


def onExitVehicle(self, player, vehicle):
    if not player.isAlive():
   		player.faa.enterVeh = 0
	return

   	    if player.faa.enterVeh > 0:
        plVehicle = player.getVehicle()
	pl_Vehicle = bf2.objectManager.getRootParent(plVehicle)
   	        if (getVehicleType(pl_Vehicle.templateName) == VEHICLE_TYPE_SOLDIER):
   	    	    player.faa.enterVeh = 0


def onPlayerKilled(self, victim, attacker, weapon, assists, object):
    if (attacker == None) or (attacker.getTeam() == victim.getTeam()) or (victim == None) or (weapon == None):
	return

    if int(noVehicles) == 1:										
	if mapName not in check_noVeh_maps:								
	    return

	if (mapName == "sharqi_peninsula") and (victim.getTeam() == 2):					
	    return
    else:
	if(victim.faa.enterVeh>0):
    	    delta = int(time.time()) - victim.faa.enterVeh
	    if int(delta) > 20:
		return

	#victimVehicle = victim.getVehicle()							
	#vic_Vehicle = bf2.objectManager.getRootParent(victimVehicle)
        #attackerVehicle = attacker.getVehicle()
	#att_Vehicle = bf2.objectManager.getRootParent(attackerVehicle)

        #attackerVehicle = bf2.objectManager.getRootParent(weapon)
	#if attacker == (attackerVehicle.isPlayerControlObject and attackerVehicle.getIsRemoteControlled()):		
	    #pass
	#else:
                   #if (getVehicleType(att_Vehicle.templateName) == VEHICLE_TYPE_SOLDIER) or (getVehicleType(vic_Vehicle.templateName) == VEHICLE_TYPE_AIRDEFENSE):
	    #return

	if attacker == victim:
                   pass
	elif attacker != None and attacker.getTeam() != victim.getTeam():
                    self.checkForSafeBase(victim, attacker, mapName, num_cp)

    if check_new_maps.has_key(mapName) and num_cp in check_new_maps[mapName]:
	self.checkForSafeBase(victim, attacker, mapName, num_cp)

    if mapName in check_old_maps:
	tx = old_baserape_maps(mapName, victim.getTeam())
	if tx.r > 0:
	    victimVehicle = victim.getVehicle()
    	    controlPoints = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
	    	    for cp in controlPoints:
   			if cp.cp_getParam('unableToChangeTeam') != 0 and cp.cp_getParam('team') != attacker.getTeam():
       		    distanceTo = self.getVectorDistance(victimVehicle.getPosition(), cp.getPosition())
    		    if float(distanceTo) < tx.r:
   				mm_utils.msg_server (" §3" + attacker.getName() + " -  §C1001 Jangan Pantek Cok §C1001")
   				self.mm.info("BASERAPE! att=" + str(attacker.getName()) + " vic=" + str(victim.getName()) +" Radius=" + str(tx.r) + " Distance=" + str(distanceTo) )
   		    		self.justify(attacker, victim)


def checkForSafeBase(self, victim, attacker, mapName, num_cp):
    victimVehicle = victim.getVehicle()
    coor_X = victimVehicle.getPosition()[0]
    coor_Y = victimVehicle.getPosition()[2]
    coor_Z = victimVehicle.getPosition()[1]

    tx = new_baserape_maps(mapName, num_cp, victim.getTeam())
    for cp in tx.tch_x:
        if (float(coor_Z) > cp['z']) and (float(coor_Z) < (cp['z'] + cp['h'])):
    	    dist = math.sqrt( (float(coor_X) - float(cp['x']))**2 + (float(coor_Y) - float(cp['y']))**2 )
    	    if float(dist) < cp['r']:
	    	if cp.has_key('point'):
    		    attackerVehicle = attacker.getVehicle()
		    att_Vehicle = bf2.objectManager.getRootParent(attackerVehicle)
	  	    if ((getVehicleType(att_Vehicle.templateName) == VEHICLE_TYPE_ARMOR) or (getVehicleType(att_Vehicle.templateName) == VEHICLE_TYPE_TRANSPORT)):
			return

		    for obj in bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint'):
			namepoint = obj.templateName.lower()[cp['c']:]
			if (namepoint == cp['point']):
			    ownerteam = int(obj.cp_getParam('team'))
			    if (ownerteam != cp['owner']):
				return

   			mm_utils.msg_server(" §3" + attacker.getName() + " -  §C1001 Jangan Pantek Cok §C1001")
   			self.mm.info("BASERAPE! att=" + str(attacker.getName()) + " vic=" + str(victim.getName()) +" Radius=" + str(cp['r']) + " Distance=" + str(dist) )
   		    	self.justify(attacker, victim)


def justify(self, attacker, victim):
           vehicle = attacker.getVehicle()
           rootVehicle = getRootParent(vehicle)

   	    victim.timedeath = int(time.time())
    victim.score.deaths += -1
    attacker.score.kills += -2
    attacker.score.score += -6  #- attacker.faa.warning
    #attacker.score.TKs += 1
    attacker.faa.warning += 1
    #if getVehicleType(rootVehicle.templateName) != VEHICLE_TYPE_SOLDIER:
              # attacker.faa.warning +=1
           #if attacker.faa.warning > 3:
               #victim.score.deaths += -1
               #attacker.score.kills += -2
               #attacker.score.score += -4 - attacker.faa.warning
            #   attacker.score.TKs += 1
    #vehicle = aattacker.getVehicle()
    #rootVehicle = getRootParent(vehicle)
    #if getVehicleType(rootVehicle.templateName) == VEHICLE_TYPE_SOLDIER:                
               #attacker.faa.warning += 1
    #if getVehicleType(rootVehicle.templateName) != VEHICLE_TYPE_SOLDIER:
	#attacker.faa.warning += 1
    if attacker.isAlive():
   		#vehicle = attacker.getVehicle()
   		#rootVehicle = getRootParent(vehicle)
   		#if getVehicleType(rootVehicle.templateName) != VEHICLE_TYPE_SOLDIER:
                #       attacker.faa.warning += 1
   		if getVehicleType(rootVehicle.templateName) != VEHICLE_TYPE_SOLDIER:
                       #attacker.faa.warning += 1
		rootVehicle.setDamage(0.01)        	
	#else:
                       #attacker.faa.warning += 1
                       #rootVehicle.setDamage(1) 
    if attacker.isCommander():
       	team = attacker.getTeam()
	enemyteam = 3 - team
	attacker.setTeam(enemyteam)
	attacker.setTeam(team)
    if attacker.faa.warning > 4:
               #victim.score.deaths += -1
	#attacker.score.kills += -2
	#attacker.score.score += -4
	#attacker.score.TKs += 1
	#attacker.faa.warning += 1
               mm_utils.msg_server (" -  §3 §C1001 Nah Kan Batoe Seh Loe §C1001")
               host.rcon_invoke('game.sayall "Player %s kicked for violating of the no kill rules within safe base area"' % (attacker.getName() ) )
               #host.rcon_invoke('admin.kickPlayer  "%s" %i "You kicked for violating of the no kill rules within safe base area"' % str(attacker.index)) #(attacker.getName(), 15) )
	host.rcon_invoke("admin.kickPlayer " + str(attacker.index))

def getVectorDistance(self, pos1, pos2):
    diffVec = [0.0, 0.0, 0.0]
    diffVec[0] = math.fabs(pos1[0] - pos2[0])
    diffVec[1] = math.fabs(pos1[1] - pos2[1])
    diffVec[2] = math.fabs(pos1[2] - pos2[2])

           return math.sqrt(diffVec[0] * diffVec[0] + diffVec[1] * diffVec[1] + diffVec[2] * diffVec[2])


def onGameStatusChanged( self, status ):
    if status == bf2.GameStatus.Playing:
	global num_cp, mapName, noVehicles
        controlPoints = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
	num_cp = len(controlPoints)
	mapName = bf2.gameLogic.getMapName()
   		noVehicles = int(bf2.serverSettings.getnoVehicles())
	for player in bf2.playerManager.getPlayers():
   		    player.faa.timedeath = 0
   		    player.faa.warning = 0
   		    player.faa.enterVeh = 0


def onPlayerRevived(self, attacker, victim): 
    if int(attacker.timedeath) > 0:
        timex = int(time.time()) - int(attacker.timedeath)
	if int(timex) < 16:
	    attacker.score.deaths += 1
	    attacker.timedeath = 0


def onPlayerConnect(self, player):
    player.faa = fStt(player)


def init( self ):
    host.registerGameStatusHandler( self.onGameStatusChanged )

    if 0 == self.__state:
               host.registerHandler('PlayerConnect', self.onPlayerConnect, 1 )
               host.registerHandler('PlayerKilled', self.onPlayerKilled )
	host.registerHandler('PlayerRevived', self.onPlayerRevived )
               host.registerHandler('EnterVehicle', self.onEnterVehicle  )
               host.registerHandler('ExitVehicle', self.onExitVehicle )

    self.__state = 1


def mm_load( modManager ):
"""Creates and returns your object."""
return new_baserape2( modManager )