from Track import Track
import math
from Vector import Vector
class ClusterPhiEtaFinderGauthamAnne():

 def find_phi_eta(self, cluster):
     totalE=0
     total_x=0
     total_y=0
     total_z=0
     weighted_x = 0
     weighted_y = 0
     weighted_z = 0

 for point in cluster.cal_hits:
     position = point.position
     x=position.x
     y=position.y
     z=position.z
     energy=point.energy
     if energy <= 0:
         continue
     totalE += energy
     total_x += x*energy
     total_y += y*energy
     total_z += z*energy
     weighted_x = total_x/(totalE)
     weighted_y= total_y/(totalE)
     weighted_z = total_z/(totalE)

    weighted_point = Vector(weighted_x, weighted_y,weighted_z)
 phi = weighted_point.azimuthal()
 while phi < 0:
     phi += 2 * math.pi
 while phi >= 2 * math.pi:
     phi -= 2 * math.pi

 if weighted_point.magnitude() ==0:
     eta = 0
 else:
     eta = weighted_point.pseudorapidity()

 return phi, eta
