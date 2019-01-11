import sys
import subprocess
import inspect
import os
import shutil
import json
import time

# Kicks off an instance of Unity to perform a build.

########################################################################################################

UNITY_VERSION = "2018.2.9f1"
UNITY_PATH = r "D:\Unity\2018.2\2018.2.9f1_2207421190e9\Editor\Unity.exe"#.format(UNITY_VERSION)
SCRIPT_PATH = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
PROJECT_PATH = SCRIPT_PATH + "/.."
LOG_PATH = PROJECT_PATH + "/Build/BuildLog.log"

########################################################################################################

def main():
	doUnityBuild()
	
########################################################################################################

def doUnityBuild():
	args = sys.argv;

	# Add the subprocess parameters.
	# The path to the program being launched needs to be the first element in the array.
	args.insert(0, UNITY_PATH)

	# The rest can go anywhere in the array, so just add them to the end.
	args.append("-quit")
	args.append("-batchmode")
	args.extend(["-projectPath", PROJECT_PATH])
	args.extend(["-executeMethod", "Build.MyBuild"])
	args.extend(["-logFile", LOG_PATH])

	doCmd(args, "Build")

########################################################################################################

def doCmd(args, logText = ""):
	#argsString = " ".join(args)
	#print argsString

	startTime = time.time()

	proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#proc = subprocess.Popen(argsString, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output = proc.communicate()[0]

	#if logText != "":
	#	print "{}{} finished in {} seconds.".format(output, logText, round(time.time() - startTime, 1))

########################################################################################################

# Do stuff after defining everything above.
main()
