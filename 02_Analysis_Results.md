# Alalysis Results 

The TMVA class in ROOT contains a function (<i> TMVA::TMVAGui</i>) that allows to call a series of macros that analyze the content of the output producing graphs and histograms relative to the analysis. It is useful to use this plots to analyze the results of the multivariate analysis.<br>In this work it was decided to slightly modify these macros (the relative files are saved [here](https://github.com/gianpierovignola/project/tree/master/JSROOT)) the outputs produced were then uploaded to a server where JSROOT was installed ([Files_on_server](https://github.com/gianpierovignola/project/tree/master/JSROOT/Files_on_server)). By <b>clicking on the images</b> presented here it is possible to access the related display in JSROOT and is possible to use the interactive reading of the results described in the [Introduction](https://github.com/gianpierovignola/project/blob/master/00_Introduction.md).

## 1.Monte Carlo Simulation

Before analyzing the results, it is useful to describe the trees used as a simulation of decay events Λ<sub>c</sub><sup>+</sup> → p+K<sub>s</sub> (signal and background).<br>
The simulation was carried out with the AliRoot(1) framework using the event generator HIJING(2)(Pb-Pb collisions) + PYTHIA(3)(p-p collisions). Using GEANT3(4), the response of the entire ALICE detector was then evaluated and 2 trees of Signal and Backgrouns were generated containing all the available measurements with the detectors. The output file of simulation (AnalysisResults.root) cannot be shared due to size and copyright issues. Thanks to prof. Andrea Alici for making this database available. <br>
The table summarizes the number of simulated events used for this analysis:

|Description|Number|
|-----------|------|
Total number of Signal events|1762028
Total number of Background events|1473789
total number of Signal events in the selected range (Λ<sub>c</sub><sup>+</sup>Pt <6 && Λ<sub>c</sub><sup>+</sup>Pt> 4)|499411
total number of Background events in the selected range (Λ<sub>c</sub><sup>+</sup>Pt <6 && Λ<sub>c</sub><sup>+</sup>Pt> 4)|252957
actual number of Signal events used for the Training|100000
actual number of Background events used for the Training|126478
actual number of Signal events used for the Test|100000
actual number of Background events used for the Test|126478


#### References
1) ALICE Collaboration, AliRoot, ALICE Offline framework for simulation, reconstruction and analysis, [http://alice-offline.web.cern.ch/](http://alice-offline.web.cern.ch/)<br>
2) X.N Wang and M. Gyulassy, HIJING: a Monte Carlo model for multiple jet production in pp, p-A and A-A collisions, Phys. Rev. D44 (1991) 3501<br>
3) T. Sjöstrand, S. Mrenna and P.Z. Skands, PYTHIA 6.4 physics and manual, JHEP 05 (2006) 026 [hep-ph / 0603175]<br>
4) R. Brun et al., GEANT detector description and simulation tool, CERN-W-5013 (1994)<br>


## 2.Input Variables 

Not all variables contained in the <b>AnalysisResults.root</b> input file were used for the multivariate analysis. It was decided to limit the number of variables to 8 and to add various spectator variables for any future analysis on the output file produced (see paragraph 2. in [TMVA_Program](https://github.com/gianpierovignola/project/blob/master/01_TMVA_Program.ipynb)).<br>
Below is a brief description of the variables that it was decided to use in the multivariate analysis:

* <b> massK0S </b>: Invariant mass of the K<sub>s</sub><sup>0</sup> particle decaying into π <sup>+</sup> and π <sup>-</sup>. From the impulse of the two daughter particles it is possible to calculate the mass of the parent particle.<br><br>

* <b>CosThetaStar</b>: cosine of the angle between the direction of emission of the proton (in the reference system in which Λ<sub>c</sub><sup>+</sup> is at rest) and the direction of Λ<sub>c</sub><sup>+</sup> in the LAB system. <br> <br>
* <b>combinedProtonProb</b>: Probability that the charged trace associated with K<sub>s</sub><sup>0</sup> is a proton. <br> <br>
* <b>signd0</b>: Proton impact parameter that takes into account the sign.<br><br>
* <b>tImpParV0</b>: Impact parameter of K<sub>s</sub><sup>0</sup><br><br>
* <b>tImpParBach</b>: Proton impact parameter defined as the distance between the reconstructed trace and the primary vertex (small for Signal events) <br> <br>
* <b>CtK0S</b>: (DecayLengthK0S * 0.497 / v0P) life-time of the K<sub>s</sub><sup>0</sup>, corresponds to the distance traveled by the K<sub>s</sub><sup>0</sup> multiplied by its mass and divided by its impulse. <br> <br>
* <b>cosPAK0S</b>: cosine of the pointing angle: angle between the reconstructed trace of the K<sub>s</sub><sup>0</sup> and the line passing through the primary vertex and that of decay of the K<sub>s</sub><sup>0</sup> (close to 1). <br> <br>

The comparison between signal and background of the input variables is represented in the following graphs (<b>click on it to open the view in JSROOT</b>). The two canvases were obtained using the macro written in pyROOT [macro.py](https://github.com/gianpierovignola/project/blob/master/JSROOT/macro.py).
<br><br>
<table cellspacing="0" cellpadding="0" width="70%">
<tr><td>
    <a href="https://jsrootsoftwareandcomputing.000webhostapp.com/rootfile/Input_Variables_1.html" target="_blank"> 
        <img src="img/Input_Variables_1.jpg" width="100%" align="center" title="Input_Variables_1.jpg">
    </a>
</td><td>
    <a href="https://jsrootsoftwareandcomputing.000webhostapp.com/rootfile/Input_Variables_2.html" target="_blank"> 
        <img src="img/Input_Variables_2.jpg" width="100%" align="center" title="Input_Variables_2.jpg">
    </a>
</td></tr>
</table>
<a href="https://root.cern/js/latest/?nobrowser&file=../files/hsimple.root&item=ntuple;1&opt=px:py::pz%3E4"><img src="https://root.cern/js/files/img/ttree.png" align="left" hspace="10" vspace="6" alt="TTree::Draw()" title="2-dimensional TTree::Draw with cut options"></a>

## 3.Correlation Coefficents 
## 4.Classifier Output
## 5.Cuts
## 6.ROC Curves 
## 7.Graphical Representation of BDT and MLP
