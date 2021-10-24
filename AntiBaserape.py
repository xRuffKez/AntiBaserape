import host
import bf2
import math
from bf2.stats.constants import *
from bf2 import g_debug

DEFAULT_SAFEBASE_RADIUS = 40 # Default safe area radius (normal commandpoint radius = 10)
ALLOWED_SAFEBASEKILLS = 3
SAFEBASEKILL_TIMER_INTERVAL = 120 # Intervals between removing a point from players.baseRapeWarning

WarnReduceTimer = None # Timer that reduces the warnings at intervals

def init():
  if g_debug: print "AntiBaserape init"
  host.registerHandler('PlayerConnect', onPlayerConnect, 1)   
  host.registerHandler('PlayerKilled', onPlayerKilled)

  # Start the timer that reduces warnings on the SAFEBASEKILL_TIMER_INTERVAL
  WarnReduceTimer = bf2.Timer(onSafeBaseKillTimer, SAFEBASEKILL_TIMER_INTERVAL, 1)
  WarnReduceTimer.setRecurring(SAFEBASEKILL_TIMER_INTERVAL)

  # Connect already connected players if reinitializing
  for p in bf2.playerManager.getPlayers():
     onPlayerConnect(p)

def onPlayerConnect(player):
  resetPlayer(player)

def onPlayerKilled(victim, attacker, weapon, assists, object):
  # killed by self
  if attacker == victim:
     pass

  # killed by enemy
  elif attacker != None and attacker.getTeam() != victim.getTeam():
     checkForSafeBase(attacker, victim)

def resetPlayer(player):
  player.baseRapeWarning = 0

def checkForSafeBase(attacker, victim):
  victimVehicle = victim.getVehicle()
  controlPoints = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
  for cp in controlPoints:
     if cp.cp_getParam('unableToChangeTeam') != 0 and cp.cp_getParam('team') != attacker.getTeam():
        distanceTo = getVectorDistance(victimVehicle.getPosition(), cp.getPosition())
        if DEFAULT_SAFEBASE_RADIUS > float(distanceTo):
           justify(attacker, victim, cp, distanceTo)

def justify(attacker, victim, controlPoint, distanceTo):
  victim.score.deaths += -1
  attacker.score.kills += -1
  attacker.score.score += -2 - attacker.baseRapeWarning
  attacker.baseRapeWarning += 1
  sendWarning(attacker, controlPoint, distanceTo)
  if attacker.baseRapeWarning > ALLOWED_SAFEBASEKILLS:
     attacker.score.TKs += 1
     if attacker.isAlive():
        vehicle = attacker.getVehicle()
        rootVehicle = getRootParent(vehicle)
        if getVehicleType(rootVehicle.templateName) == VEHICLE_TYPE_SOLDIER:
           rootVehicle.setDamage(0)
        else:
           rootVehicle.setDamage(1)

def sendWarning(player, controlPoint, distanceTo):
  mapName = bf2.gameLogic.getMapName()
  if player.baseRapeWarning > ALLOWED_SAFEBASEKILLS:
     sendMsgAll(player.getName() + " is punished for repeated violating of the no kill rules within safe base area")
  else:
     sendMsgAll(player.getName() + " has violated of the no kill rules within safe base area " + str(player.baseRapeWarning) + " times now")

def onSafeBaseKillTimer(data):
  for p in bf2.playerManager.getPlayers():
     if p.baseRapeWarning > 0: p.baseRapeWarning -= 1

def getVectorDistance(pos1, pos2):
  diffVec = [0.0, 0.0, 0.0]
  diffVec[0] = math.fabs(pos1[0] - pos2[0])
  diffVec[1] = math.fabs(pos1[1] - pos2[1])
  diffVec[2] = math.fabs(pos1[2] - pos2[2])

  # Application of Pythagorean theorem to calculate total distance
  return math.sqrt(diffVec[0] * diffVec[0] + diffVec[1] * diffVec[1] + diffVec[2] * diffVec[2])

def sendMsgAll(msg):
  host.rcon_invoke("game.sayAll \"" + str(msg) + "\"")
