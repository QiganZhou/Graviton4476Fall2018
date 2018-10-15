import numpy as np
from helper import *
import matplotlib.pyplot as plt


# Represents a labelled time-frequency map.
class TfMap(object):
	# @param waveName (str): an example is "GT0577".
	# @param iota (float): the inclination angle.
	# @param phi (float): the azimuthal angle.
	# @param timeArr (1-D numpy array of dtype np.float64):
	# 	the time array.
	# @param freqArr (1-D numpy array of dtype np.float64):
	#	the frequency array.
	# @param intensityArr (2-D numpy array of dtype np.float64):
	# 	the intensity array.
	# @param chirpNum (int) : the number of chirps identified for this
	# 	time-frequency map.
	# @param chirpTimes (1-D numpy array of dtype np.float64):
	#	the times corresponding to the identified chirps.
	def __init__(self, waveName, iota, phi,
				 timeArr, freqArr, intensityArr,
				 chirpNum, chirpTimes, strongCheck=True):
		assert waveName.find(".") == waveName.find("/") == -1
		assert waveName[:2] == "GT"
		assert type(iota) == float
		assert type(phi) == float
		if strongCheck:
			assert type(timeArr) == np.ndarray
			assert type(freqArr) == np.ndarray
			assert type(intensityArr) == np.ndarray
			assert type(chirpNum) == int
			assert type(chirpTimes) == np.ndarray
			assert timeArr.dtype == np.float64
			assert freqArr.dtype == np.float64
			assert intensityArr.dtype == np.float64
			assert timeArr.ndim == freqArr.ndim == 1
			assert intensityArr.ndim == 2
			assert intensityArr.shape[0] == freqArr.shape[0]
			assert intensityArr.shape[1] == timeArr.shape[0]
			assert chirpTimes.dtype == np.float64
			assert chirpTimes.ndim == 1
			assert chirpNum == len(chirpTimes)
		self.waveName = waveName
		self.iota = iota
		self.phi = phi
		self.timeArr = timeArr
		self.freqArr = freqArr
		self.intensityArr = intensityArr
		self.chirpNum = chirpNum
		self.chirpTimes = chirpTimes

	# This method is designed for comparing the iota angles.
	# This is because comparing floats can be tricky due to
	# precision problems. For example, 1.0 + 2.0 != 3.0.
	def iotaRound(self, ndigits=6):
		return round(self.iota, ndigits=ndigits)

	def phiRound(self, ndigits=6):
		return round(self.phi, ndigits=ndigits)

	# The __eq__, __ne__, and __hash__ methods are rewritten
	# to make TfMap objects capable of working with sets.
	def __eq__(self, other):
		if isinstance(other, TfMap):
			return self.waveName == other.waveName and \
				self.iotaRound() == other.iotaRound() and \
				self.phiRound() == other.phiRound()
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	# Rewritten to make TfMap objects sortable.
	def __cmp__(self, other):
		if cmp(self.waveName, other.waveName) != 0:
			return cmp(self.waveName, other.waveName)
		elif cmp(self.iotaRound(), other.iotaRound()) != 0:
			return cmp(self.iotaRound(), other.iotaRound())
		else:
			return cmp(self.phiRound(), other.phiRound())

	def __hash__(self):
		# Returning the hash of a 3-tuple.
		return hash((self.waveName, self.iotaRound(),
					 self.phiRound()))

	def __str__(self):
		return "{}, iota: {}, phi: {}.".format(self.waveName,
											  angToStr(self.iota),
											  angToStr(self.phi))

	def __repr__(self):
		return self.__str__()

	# Plot and show the time-frequency map.
	def showPlot(self):
		plt.pcolormesh(self.timeArr, self.freqArr,
					   self.intensityArr, cmap="gray")
		plt.xlabel("time (s)")
		plt.ylabel("frequency (Hz)")
		plt.title("{}, iota: {}, phi: {}".format(self.waveName,
											  angToStr(self.iota),
											  angToStr(self.phi)))
		plt.show()
