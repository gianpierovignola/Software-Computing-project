# Software-Computing-project

The aim of this work is to analyze simulated montecarlo data (Signal and Background) of a decay channel of the charmed Λ<sub>c</sub><sup>+</sup> baryon using the ROOT TMVA tool. The [main code](https://github.com/gianpierovignola/project/blob/master/01_TMVA_Program.ipynb) is written in python using Python-C ++ bindings, called PyROOT. <br>
The results were then analyzed by modifying some [ROOT macros](https://github.com/gianpierovignola/project/tree/master/JSROOT) and [presented](https://github.com/gianpierovignola/project/blob/master/02_Analysis_Results.md) with JavaScript ROOT (JSROOT) installed using a free hosting service on a dedicated server: [jsrootsoftwareandcomputing](Https://jsrootsoftwareandcomputing.000webhostapp.com/).

# Folders in the repository

* [<b>JSROOT</b>](https://github.com/gianpierovignola/project/tree/master/JSROOT): this folder contains the macros used to produce the TMVA output plots and a folder with the .root files and .html pages uploaded to the server.
* [<b>References</b>](https://github.com/gianpierovignola/project/tree/master/References): this folder contains the references used. 
* [<b>Results</b>](https://github.com/gianpierovignola/project/tree/master/Results): this folder contains the results of the TMVA analysis. It includes the <i>TMVA_output.root</i> file and <i>std_output.txt</i> produced By [main program](https://github.com/gianpierovignola/project/blob/master/01_TMVA_Program.ipynb). There is also a folder containing the weights of Cuts, MLP and BDT produced during training.
* [<b>img</b>]: this folder contains images used in the [introduction](https://github.com/gianpierovignola/project/blob/master/00_Introduction.md) and [Analysis Results](https://github.com/gianpierovignola/project/blob/master/02_Analysis_Results.md).
* [<b>00_Introduction.md</b>](https://github.com/gianpierovignola/project/blob/master/00_Introduction.md):introduction to the project.
* [<b>01_TMVA_Program.ipynb</b>](https://github.com/gianpierovignola/project/blob/master/01_TMVA_Program.ipynb): main program in pyROOT with comments.
* [<b>02_Analysis_Results.md</b>](https://github.com/gianpierovignola/project/blob/master/02_Analysis_Results.md): analysis of the results with links to the JSROOT plots.
