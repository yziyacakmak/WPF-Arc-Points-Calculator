# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:00:31 2022

@author: yusuf.cakmak
"""
import math as mt
#def final(diameter,pointX,pointY):
    
    
#offsetX=input("please enter the offset of gauge on X axis: ")
#offsetY=input("please enter the offset of gauge on Y axis: ")
#diameter=input("please enter the diameter of gauge: ")
# offsetX=30
# offsetY=30
# diameter=386
# strokeThickness=input("please enter the stroke thickness of gauge: ")
# startPointAngle=input("please enter the start point angle in clokwise direction: ")
# angleBetweenPoints=input("please enter the angle between points in clokwise direction: ")
# offsetX=float(offsetX)
# offsetY=float(offsetY)
# startPointAngle=float(startPointAngle)
# angleBetweenPoints=float(angleBetweenPoints)
# diameter=float(diameter)
# strokeThickness=float(strokeThickness)
# hstrokeThickness=strokeThickness/2
# radius=diameter/2


#radius=(radius+strokeThickness)
def function():
    offsetX=30
    offsetY=30
    diameter=386
    strokeThickness=input("please enter the stroke thickness of gauge: ")
    startPointAngle=input("please enter the start point angle in clokwise direction: ")
    angleBetweenPoints=input("please enter the angle between points in clokwise direction: ")
    offsetX=float(offsetX)
    offsetY=float(offsetY)
    startPointAngle=float(startPointAngle)
    angleBetweenPoints=float(angleBetweenPoints)
    diameter=float(diameter)
    strokeThickness=float(strokeThickness)
    hstrokeThickness=strokeThickness/2  #half stroke thickness
    radius=diameter/2
    if startPointAngle>90 and startPointAngle<180:
       startPointX=offsetX+radius-mt.sin(mt.radians(startPointAngle-90))*radius+hstrokeThickness*mt.sin(mt.radians(startPointAngle-90))
       startPointY=offsetY+radius+mt.cos(mt.radians(startPointAngle-90))*radius-hstrokeThickness*mt.cos(mt.radians(startPointAngle-90))
       endPointX=offsetX+radius-mt.sin(mt.radians(startPointAngle-90+angleBetweenPoints))*radius+hstrokeThickness*mt.sin(mt.radians(startPointAngle-90+angleBetweenPoints))
       endPointY=offsetY+radius+mt.cos(mt.radians(startPointAngle-90+angleBetweenPoints))*radius-hstrokeThickness*mt.cos(mt.radians(startPointAngle-90+angleBetweenPoints))
    elif startPointAngle>=0 and startPointAngle<=90:
        startPointX=offsetX+radius+mt.cos(mt.radians(startPointAngle))*radius-hstrokeThickness*mt.cos(mt.radians(startPointAngle))
        startPointY=offsetY+radius+mt.sin(mt.radians(startPointAngle))*radius-hstrokeThickness*mt.sin(mt.radians(startPointAngle))
        endPointX=offsetX+radius+mt.cos(mt.radians(startPointAngle+angleBetweenPoints))*radius-hstrokeThickness*mt.cos(mt.radians(startPointAngle+angleBetweenPoints))
        endPointY=offsetY+radius+mt.sin(mt.radians(startPointAngle+angleBetweenPoints))*radius-hstrokeThickness*mt.sin(mt.radians(startPointAngle+angleBetweenPoints))
    elif startPointAngle>=180 and startPointAngle<=270:
        startPointX=offsetX+radius-mt.cos(mt.radians(startPointAngle-180))*radius+hstrokeThickness*mt.cos(mt.radians(startPointAngle-180))
        startPointY=offsetY+radius-mt.sin(mt.radians(startPointAngle-180))*radius+hstrokeThickness*mt.sin(mt.radians(startPointAngle-180))
        endPointX=offsetX+radius-mt.cos(mt.radians(startPointAngle-180+angleBetweenPoints))*radius+hstrokeThickness*mt.cos(mt.radians(startPointAngle-180+angleBetweenPoints))
        endPointY=offsetY+radius-mt.sin(mt.radians(startPointAngle-180+angleBetweenPoints))*radius+hstrokeThickness*mt.sin(mt.radians(startPointAngle-180+angleBetweenPoints))
    elif startPointAngle>270 and startPointAngle<360:
        startPointX=offsetX+radius+mt.sin(mt.radians(startPointAngle-270))*radius-hstrokeThickness*mt.sin(mt.radians(startPointAngle-270))
        startPointY=offsetY+radius-mt.cos(mt.radians(startPointAngle-270))*radius+hstrokeThickness*mt.cos(mt.radians(startPointAngle-270))
        endPointX=offsetX+radius+mt.sin(mt.radians(startPointAngle-270+angleBetweenPoints))*radius-hstrokeThickness*mt.sin(mt.radians(startPointAngle-270+angleBetweenPoints))
        endPointY=offsetY+radius-mt.cos(mt.radians(startPointAngle-270+angleBetweenPoints))*radius+hstrokeThickness*mt.cos(mt.radians(startPointAngle-270+angleBetweenPoints))
        
        
    print("Start Point: ",startPointX,startPointY)
    print("Point: ",endPointX,endPointY)
    print("Size: ",(radius-hstrokeThickness),(radius-hstrokeThickness))
    ans=input("new operation? [y/n] ")
    if ans.lower()=="y":
        function()
    else:
        print("bye ;)")

function()

