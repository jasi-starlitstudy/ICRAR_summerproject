#!/usr/bin/env python3
import sys
from astropy import units as u
from astropy.coordinates import SkyCoord
import astropy.cosmology.units as cu

# Format: run script (python)  <scriptname> <f_sum> <freq_peak>

def main():

        fsum = float(sys.argv[1])
        freq = float(sys.argv[2])
        z = 1420.40575177/freq-1
        shift = z * cu.redshift
        d = shift.to(u.Mpc, cu.redshift_distance())
        print("\n Distance: ",d)
        fS = fsum
        mass = 49.7*(d.value)**2*fS
        massfix = round(mass/(10**8),5)
        print(" Full: ",mass,"\n", "Sci: ", massfix,"x10^8 solar masses")


if __name__ == "__main__":
    main()
