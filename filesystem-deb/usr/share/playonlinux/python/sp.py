#!/usr/bin/python 
# -*- coding:Utf-8 -*- 

# Copyright (C) 2008 Pâris Quentin

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA. 


import wxversion
wxversion.select("2.8")
import wx, wx.html
import lib.Variables as Variables, sys


class MainWindow(wx.Frame):
  def __init__(self,parent,id,title):
    wx.Frame.__init__(self, parent, -1, title, size = (500, 333))
    self.SetIcon(wx.Icon(Variables.playonlinux_env+"/etc/playonlinux.png", wx.BITMAP_TYPE_ANY))
    self.img = wx.StaticBitmap(self, -1, wx.Bitmap(Variables.playonlinux_env+"/etc/photo"))

 
class PlayOnLinuxApp(wx.App):
   def OnInit(self):
	self.frame = MainWindow(None, -1, "PlayOnLinux Conceptor")
        self.SetTopWindow(self.frame)
	self.frame.Center(wx.BOTH)
       	self.frame.Show(True)
        return True



app = PlayOnLinuxApp()
app.MainLoop()
sys.exit(0)
