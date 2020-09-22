from ROOT import TCanvas
from ROOT import TFile, TCanvas, TH1F, TLegend
from ROOT import gSystem

#definitions of function
def Plot_Input_Variables():
    #remove warnings connected to not used file in the input source 
    gSystem.RedirectOutput("/dev/null") 
    #open the input file
    Finput = TFile("AnalysisResults.root")    
    #extract signal and Background trees from file
    SigTree = Finput.Get("treeList_2_25_2_25_Sgn")
    BkgTree = Finput.Get("treeList_2_25_2_25_Bkg")

    #create the canvas 
    c1 = TCanvas("c1","Distributions of input variables",900,1800)
    #divide canvas in 2x4 SubCanvas
    c1.Divide(2,4)
    #draw in the (1,1) coordinate of the canvas 
    c1.cd(1)
    #create an histogram that will contain the signal of the first variable
    h1s = TH1F("massK0S_Signal","massK0S",100,0.486,0.508)
    #some extetic corrections 
    h1s.SetStats(0)
    h1s.SetFillColor(4)
    h1s.SetFillStyle(3004)
    h1s.SetLineWidth(2);
    h1s.SetLineColor(4);
    #create an histogram that will contain the background of the first variable
    h1b = TH1F("massK0S_Background","",100,0.486,0.508)
    #some extetic corrections
    h1b.SetStats(0)
    h1b.SetFillColor(2)
    h1b.SetFillStyle(3005)
    h1b.SetLineWidth(2);
    h1b.SetLineColor(2);
    #fill the histograms with data in trees 
    SigTree.Project("massK0S_Signal","massK0S")
    BkgTree.Project("massK0S_Background","massK0S")
    #drow on Canvas
    h1s.Draw("same")
    h1b.Draw("same")  
    
    #do the same for the second variable
    c1.cd(2)
    h2s = TH1F("CosThetaStar_Signal","CosThetaStar",100,-1.05,1.05)
    h2s.SetStats(0)
    h2s.SetFillColor(4)
    h2s.SetFillStyle(3004)
    h2s.SetLineWidth(2);
    h2s.SetLineColor(4);
    h2b = TH1F("CosThetaStar_Background","",100,-1.05,1.05)
    h2b.SetStats(0)
    h2b.SetFillColor(2)
    h2b.SetFillStyle(3005)
    h2b.SetLineWidth(2);
    h2b.SetLineColor(2);
    SigTree.Project("CosThetaStar_Signal","CosThetaStar")
    BkgTree.Project("CosThetaStar_Background","CosThetaStar")
    h2s.Draw("same")
    h2b.Draw("same")  

    #do the same for the third variable
    c1.cd(3)
    h3s = TH1F("combinedProtonProb_Signal","combinedProtonProb",30,-0.1,1.1)
    h3s.SetStats(0)
    h3s.SetFillColor(4)
    h3s.SetFillStyle(3004)
    h3s.SetLineWidth(2);
    h3s.SetLineColor(4);
    h3b = TH1F("combinedProtonProb_Background","",30,-0.1,1.1)
    h3b.SetStats(0)
    h3b.SetFillColor(2)
    h3b.SetFillStyle(3005)
    h3b.SetLineWidth(2);
    h3b.SetLineColor(2);
    SigTree.Project("combinedProtonProb_Signal","combinedProtonProb")
    BkgTree.Project("combinedProtonProb_Background","combinedProtonProb")
    h3s.Draw("same")
    h3b.Draw("same")  
    
    ##do the same for the fourth variable
    c1.cd(4)
    h4s = TH1F("signd0_Signal","signd0",100,-0.01,0.14)
    h4s.SetStats(0)
    h4s.SetFillColor(4)
    h4s.SetFillStyle(3004)
    h4s.SetLineWidth(2);
    h4s.SetLineColor(4);
    h4b = TH1F("signd0_Background","",100,-0.01,0.14)
    h4b.SetStats(0)
    h4b.SetFillColor(2)
    h4b.SetFillStyle(3005)
    h4b.SetLineWidth(2);
    h4b.SetLineColor(2);
    SigTree.Project("signd0_Signal","signd0")
    BkgTree.Project("signd0_Background","signd0")
    h4s.Draw("same")
    h4b.Draw("same") 

    #do the same for the fifth variable
    c1.cd(5)
    h5s = TH1F("tImpParV0_Signal","tImpParV0",100,-0.2,0.2)
    h5s.SetStats(0)
    h5s.SetFillColor(4)
    h5s.SetFillStyle(3004)
    h5s.SetLineWidth(2);
    h5s.SetLineColor(4);
    h5b = TH1F("tImpParV0_Background","",100,-0.2,0.2)
    h5b.SetStats(0)
    h5b.SetFillColor(2)
    h5b.SetFillStyle(3005)
    h5b.SetLineWidth(2);
    h5b.SetLineColor(2);
    SigTree.Project("tImpParV0_Signal","tImpParV0")
    BkgTree.Project("tImpParV0_Background","tImpParV0")
    h5s.Draw("same")
    h5b.Draw("same") 
    
    #do the same for the sixth variable
    c1.cd(6)
    h6s = TH1F("tImpParBach_Signal","tImpParBach",100,-0.1,0.1)
    h6s.SetStats(0)
    h6s.SetFillColor(4)
    h6s.SetFillStyle(3004)
    h6s.SetLineWidth(2);
    h6s.SetLineColor(4);
    h6b = TH1F("tImpParBach_Background","",100,-0.1,0.1)
    h6b.SetStats(0)
    h6b.SetFillColor(2)
    h6b.SetFillStyle(3005)
    h6b.SetLineWidth(2);
    h6b.SetLineColor(2);
    SigTree.Project("tImpParBach_Signal","tImpParBach")
    BkgTree.Project("tImpParBach_Background","tImpParBach")
    h6s.Draw("same")
    h6b.Draw("same") 

    #do the same for the seventh variable
    c1.cd(7)
    h7s = TH1F("DecayLengthK0S_Signal","DecayLengthK0S",100,-5,100)
    h7s.SetStats(0)
    h7s.SetFillColor(4)
    h7s.SetFillStyle(3004)
    h7s.SetLineWidth(2);
    h7s.SetLineColor(4);
    h7b = TH1F("DecayLengthK0S_Background","",100,-5,100)
    h7b.SetStats(0)
    h7b.SetFillColor(2)
    h7b.SetFillStyle(3005)
    h7b.SetLineWidth(2);
    h7b.SetLineColor(2);
    SigTree.Project("DecayLengthK0S_Signal","DecayLengthK0S")
    BkgTree.Project("DecayLengthK0S_Background","DecayLengthK0S")
    h7s.Draw("same")
    h7b.Draw("same") 

    #do the same for the eighth variable
    c1.cd(8)
    h8s = TH1F("cosPAK0S_Signal","cosPAK0S",100,0.9999,1.00001)
    h8s.SetStats(0)
    h8s.SetFillColor(4)
    h8s.SetFillStyle(3004)
    h8s.SetLineWidth(2);
    h8s.SetLineColor(4);
    h8b = TH1F("cosPAK0S_Background","",100,0.9999,1.00001)
    h8b.SetStats(0)
    h8b.SetFillColor(2)
    h8b.SetFillStyle(3005)
    h8b.SetLineWidth(2);
    h8b.SetLineColor(2);
    SigTree.Project("cosPAK0S_Signal","cosPAK0S")
    BkgTree.Project("cosPAK0S_Background","cosPAK0S")
    h8s.Draw("same")
    h8b.Draw("same") 
    
    #draw legend on canvas
    c1.cd(2)
    legend = TLegend(0.7,0.9,1,0.7)
    legend.AddEntry(h1s,"Signal","f")
    legend.AddEntry(h1b,"Background","f")
    legend.Draw("same")
    #save canvas on output file
    c1.SaveAs("Input_Variables.root")