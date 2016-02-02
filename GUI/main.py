#!/usr/bin/env python
from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import rospy
from math import *
from std_msgs.msg import * #for convenience
<<<<<<< HEAD
from mainUI import *
PI = 3.14159265358979
=======
>>>>>>> 86fc243a0368d455235fdaeda17b6ced53cd5117

class ORSWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent);
<<<<<<< HEAD
        self.ui =  Ui_ORS_GUI();
        self.ui.setupUi(self);
        rospy.init_node('ORS_GUI',anonymous=True);
        self.RCRSub = rospy.Subscriber('sample_msg',Float32,self.fetchData);
        self.theta = 0;
    def fetchData(self,msg):
        print(msg.data);
        self.theta = msg.data;
        self.update();
    def update(self):
        self.ui.compass.setValue(self.theta * 180 / PI);
        self.ui.map.setLoc(self.theta,self.theta);
        QMainWindow.update(self);

=======
        uic.loadUi("main.ui",self);
        rospy.init_node('orsvisualize',anonymous=True);
        self.sub = rospy.Subscriber('sample_msg',Float32,self.fetchData);
        self.theta = 0;
    def fetchData(self,msg):
        self.theta = msg.data;
        self.update();
    def update(self):
        QMainWindow.update(self);
    def paintEvent(self,event): #example display
        QMainWindow.paintEvent(self,event);
        p = QPainter(self);
        theta = self.theta;
        poly = QPolygon();
        poly.append(QPoint(100*cos(theta),-100*sin(theta)));
        poly.append(QPoint(-30*sin(theta),-30*cos(theta)));
        poly.append(QPoint(30*sin(theta),30*cos(theta)));
        poly.append(QPoint(100*cos(theta),-100*sin(theta)));
        poly.translate(300,300);
        poly = QPolygonF(poly);
        path = QPainterPath();
        path.addPolygon(poly);
        brush = QBrush(QColor(0,128,128,255));
        p.drawPolygon(poly);
        p.fillPath(path,brush);
>>>>>>> 86fc243a0368d455235fdaeda17b6ced53cd5117
if __name__ == "__main__":
    app = QApplication(sys.argv);
    w = ORSWindow();
    w.setWindowTitle("ORSVisualize");
    w.show();
    sys.exit(app.exec_());
