# Stability-simulations
Course Project Thermodynamics of materials- Simulations to predict stability of different Iron Oxides
Codes are available both in Matlab and Python programming languages.

Please Refer this to understand the theory behind and the Readme.pdf for getting info about the codes.

This Repository contains Programs which gives stability of Fe3O4, FeO and Fe in a graph showing Temperature vs PH2/(PH2+PH20)

The Gibb’s free energy changes or ∆G of a reaction tells us the feasibility of a reaction when temperature and pressure are constant during reaction progress. The lower the value of ∆G of a reaction, the more feasible is the reaction.
This way ∆G of a reaction can also tell us the stability of a set of products and help us identify the most stable product from the set.

In this report we predict the stabilities of Fe(s), FeO(s) and Fe3O4(s). For this we use the equation –
∆G = ∆G0 + RTlnK
∆G0 = -RTlnK (this equation holds at equilibrium, when ∆G becomes 0) Thus, for the 3 reactions-
FeO(s) + H2(g) = Fe(s) + H2O (g) - (i)
Fe3O4(s) + H2(g) = 3FeO(s) + H2O(g) - (ii)
Fe3O4(s) + 4H2(g) = 3Fe(s) + 4 H2O(g) – (iii)

As we know that the equilibrium constant for all reactions –
K = (PH20/PH2) (For all these reactions when solids considered pure, for reaction (iii) a power of 4 is also there but that is taken care of when we take log in the ∆G0 equation)

Thus, we can compare stabilities of Fe(s), FeO(s) and Fe3O4(s) by comparing the values of PH2/PH20 or PH2/(PH2 + PH2O) values.

Some Other References:-
1. https://dergipark.org.tr/en/download/article-file/65710
2. https://www.researchgate.net/publication/250675802_On_the_Gibbs_energy_of_formation_of_
wustite
3. https://hal-insu.archives-ouvertes.fr/hal-00069333/document

