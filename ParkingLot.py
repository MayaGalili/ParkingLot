# -*- coding: utf-8 -*-
"""
Design a parking lot using object-oriented principles. 


Created on Wed Jul  4 09:14:28 2018
@author: Maya Galili
"""

#%%  vehicle

from random import shuffle

class Vehicle:
       
    def __init__(self,wheel_num,car_type):
        self._car_type = car_type
        self._wheel_num = wheel_num

    # getters       
    def getType(self):
        return self._car_type
    
    def getWheelNum(self):
        return self._wheel_num

class Motorcycle(Vehicle): 
        def __init__(self):
            Vehicle.__init__(self,2,'MOTORCYCLE')

class Car(Vehicle):  
        def __init__(self):
            Vehicle.__init__(self,4,'CAR')
            
class Bus(Vehicle):  
        def __init__(self):
            Vehicle.__init__(self,6,'BUS')

#%% parking lot
class ParkingLot:
    
    def __init__(self,small_spot_sz, med_spot_sz,big_spot_sz):          
        self._vehicle_set = []
        self._total_spots = self.generateOpenSpots(small_spot_sz, med_spot_sz,big_spot_sz)

    # creat a parking lot with X1 small spots, x2 medium spots and x3 big spots    
    def generateOpenSpots(self,small_spot_sz, med_spot_sz,big_spot_sz):
        self._total_spots = []   

        for i in range(small_spot_sz):
            self._total_spots.append(SmallSpot())
        for i in range(med_spot_sz):
            self._total_spots.append(MedSpot())
        for i in range(big_spot_sz):
            self._total_spots.append(BigSpot())
            
        shuffle(self._total_spots)         
        return self._total_spots
      
    # find next open spot and park the given car if posible
    # if there is no good spot, enter the next car
    def park_new_vec(self,new_vehicle):
        
        total_spots_sz = self.getTotalSpotsSz()
        for i in range(total_spots_sz):
            if self._total_spots[i].is_open():
                #set spot to hold the car
                if self._total_spots[i].park_vehicle(new_vehicle):
                    print('{} is parking in spot {} (size {}). '.format(new_vehicle.getType(), i, self._total_spots[i].getSpotSize()))
                    # add car to the parkingLot cars list
                    self._vehicle_set.append(new_vehicle)
                    break
                
    def is_park_open(self):
        return (self.getOpenSpotsSz() > 0)
    
    # getters
    def getTotalSpotsSz(self):
        return len(self._total_spots)
    
    def getVehicleSet(self):
        return self._vehicle_set
    
    def getOpenSpotsSz(self):
        return self.getTotalSpotsSz() - len(self.getVehicleSet())
    
    def getAllSpots(self):
        return self._total_spots

#%%  spot
            
class Spot:
    
    def __init__(self,spot_sz):
        self._spot_size = spot_sz
        self._spot_car = None
        
    def is_open(self):
        return self._spot_car == None
    
    def park_vehicle(self,new_vec):
        can_park = new_vec.getWheelNum()/2 <= self.getSpotSize()
        if can_park:
            self._spot_car = new_vec
        return can_park              

    # getters        
    def getParkedVec(self):
        return self._spot_car
    
    def getSpotSize(self):
        return self._spot_size    
    
class SmallSpot(Spot):
    def __init__(self):
        Spot.__init__(self,1)
    
class MedSpot(Spot):
    def __init__(self):
        Spot.__init__(self,2)
        
class BigSpot(Spot):
    def __init__(self):
        Spot.__init__(self,3)
#%%
                              
''' running example:
1) creat the parking lot with X1 small spots, x2 medium spots and x3 big spots
2) creat a set of vihacles with y1 bickles y2 cars and y3 busses
3) for each vihacle in its turn - 
    find a suitable sopt and park it
    first randomly and at the next code iteration try to consider other vehicles
'''
# creat the parking lot
small_spot_sz= 2
med_spot_sz = 10
big_spot_sz = 2

PL = ParkingLot(small_spot_sz, med_spot_sz,big_spot_sz)

# creat a rand set of vihacles   
cycle_sz = 2
cars_sz = 5
buses_sz = 1

vec_set = []
for i in range(cycle_sz):
    vec_set.append(Motorcycle())
for i in range(cars_sz):
    vec_set.append(Car())            
for i in range(buses_sz):
    vec_set.append(Bus())
shuffle(vec_set)

# try to park all cars
for i in range (len(vec_set)):
    PL.park_new_vec(vec_set[i])