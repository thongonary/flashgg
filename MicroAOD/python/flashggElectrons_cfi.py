import FWCore.ParameterSet.Config as cms

flashggElectrons = cms.EDProducer('FlashggElectronProducer',
		verbose = cms.untracked.bool(False),
		electronTag = cms.InputTag('slimmedElectrons'),
		vertexTag = cms.InputTag('offlineSlimmedPrimaryVertices'),
		convTag   = cms.InputTag('reducedEgamma','reducedConversions'),
                beamSpotTag = cms.InputTag( "offlineBeamSpot" ),
		reducedEBRecHitCollection = cms.InputTag('reducedEcalRecHitsEB'),
		reducedEERecHitCollection = cms.InputTag('reducedEcalRecHitsEE'),
		rhoFixedGridCollection = cms.InputTag('fixedGridRhoAll'),
                mvaValuesMap = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
                mvaNoIsoValuesMap = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                effAreasConfigFile = cms.FileInPath("RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt"),
  		eleMVAMediumIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring15-25ns-nonTrig-V1-wp90"),
                eleMVATightIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring15-25ns-nonTrig-V1-wp80"),
                eleVetoIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),   
                eleLooseIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
                eleMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
                eleTightIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
                eleHEEPIdMap = cms.InputTag("egmGsfElectronIDs:heepElectronID-HEEPV60"),
                eleMVALooseIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wpLoose"),
                eleMVALooseNoIsoIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wpLoose"),
                eleMVAMediumNoIsoIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wp90"),
                eleMVATightNoIsoIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wp80"),
		pfCandidatesTag = cms.InputTag("packedPFCandidates"),

		elecminiso_r_min = cms.double(0.05),
		elecminiso_r_max = cms.double(0.2),
		elecminiso_kt_scale = cms.double(10.0),
		elecEBminiso_deadcone_ch = cms.double(0.0),
		elecEBminiso_deadcone_pu = cms.double(0.0),
		elecEBminiso_deadcone_ph = cms.double(0.0),
		elecEBminiso_deadcone_nh = cms.double(0.0),
		elecEEminiso_deadcone_ch = cms.double(0.015),
                elecEEminiso_deadcone_pu = cms.double(0.015),
                elecEEminiso_deadcone_ph = cms.double(0.08),
                elecEEminiso_deadcone_nh = cms.double(0.0),
		elecminiso_ptThresh = cms.double(0.0)
		)
