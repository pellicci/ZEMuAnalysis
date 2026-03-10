
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection

class Preselector(Module):
	def __init__(self, runningEra):
		self.runningEra = runningEra
		pass

	def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):

		self.out = wrappedOutputTree

		if self.runningEra > 3 :
			self.out.branch("Photon_mass", "F", lenVar="nPhoton") # Hack so that photon.p4() works

	def analyze(self, event):

		Photons = Collection(event, "Photon")

		fsrM = [0.]*len(Photons)
		if self.runningEra > 3 :
			self.out.fillBranch("Photon_mass", fsrM)
		
		return True

