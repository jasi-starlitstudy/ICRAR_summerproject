## Scripts written for ICRAR summer studentship project Streamlining Galaxy Discovery

HImass_calculator uses astropy and results in the SoFiA _cat.txt file to produce the distance for a given galaxy as well as the HI mass. It takes in two arguments, the first being the f_sum value (this is the observed flux) and the second being freq_peak (peak frequency for a detection).

SourceList_make takes in a region file produced by CARTA (.CRTF) and retrieves the RA, Dec, region number, shape of the region (ellipse or rectangular) and the region name, should one be specified. The region name appears in the final column under "Notes".
Please be aware that should a comma ',' be used in the region name in CARTA, the script may not produce the desired output for that region.
