#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ExampleTooltips.py
#
#  Copyright 2018  Bill Williams
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import datetime

try:
	from Tkinter import *	# Python 2.X
	from 		tkColorChooser import askcolor
	import 	tkFileDialog as FileDialog
	import 	tkMessageBox as MessageBox
	import 	ttk
	from 		ttk import *
	import 	tkFont	as Font
except ImportError:
	from tkinter import *	# Python 3.X
	from		tkinter.colorchooser import askcolor
	import	tkinter.filedialog as FileDialog
	import	tkinter.messagebox as MessageBox
	from		tkinter import ttk
	from 		tkinter.ttk import *
	import	tkinter.font	as Font

from Tooltip import *

'''
	Main function to display the form with various controls, and attach
	a ToolTip widget to the controls. Deomstrates how to load the
	ToolTip file, add ToolTips using message numbers, and how to create
	ToolTips that use a function callback to get the tooltip text.

	The function also demonstrates how to show/hide Tooltips and ToolTip
	number under programmer control, and how to vary the ToolTop show delay
	under program control.
'''
class TooltipTest ( Frame ):
	def __init__(self, root, title):
		Frame.__init__(self, root)
		root.title(title)
		root.config(padx=15,pady=15)

		# Load the tooltips. If None is specified, then the file 'Tooltips.txt'
		# must be in the same directory as this file. Or, pass a /path/filename
		ToolTip.LoadToolTips(None)

		# Any widget can be assigned a Tooltip.

		f = ttk.LabelFrame(root,text="Tooltip test widgets",padding=(5,5,5,5))
		f.grid(row=0,column=0,sticky='NSEW',padx=(0,10))
		for i in range(5):
			b = ttk.Button(f,text='Press Me: Tip %d'%(100+i),command=self.PressMe)
			b.grid(row=i,column=0,pady=(0,5),sticky='W')
			ToolTip(b,100+i)	# Tips numbered 100 to 104

		f = ttk.LabelFrame(root,text="Tooltip test widgets",padding=(5,5,5,5))
		f.grid(row=0,column=1,sticky='NSEW')
		for i in range(5):
			b = ttk.Checkbutton(f,text='Check button: Tip %d'%(200+i),command=self.PressMe)
			b.grid(row=i,column=0,pady=(0,5),sticky='W')
			ToolTip(b,200+i)	# Tips numbered 200 to 204

		f = ttk.LabelFrame(root,text="Control the tooltips",padding=(5,5,5,5))
		f.grid(row=1,column=0,rowspan=2,sticky='NSEW')

		b = BooleanVar()
		# This is a static variable, so you must reference it by module name
		b.set(ToolTip.ShowToolTips)	# The defaut value is True
		c = ttk.Checkbutton(f,text='Enable tooltips',variable=b,
			command=self.HideTooltipsPressed)
		c.grid(row=0,column=0,pady=(0,5),sticky='W')
		ToolTip(c,9999)	# If no matching tip number is found, then the
								# tip message states that

		b = BooleanVar()
		# This is a static variable, so you must reference it by module name
		b.set(ToolTip.ShowTipNumber)	# The defaut value is False
		c = ttk.Checkbutton(f,text='Show tip number in tooltip',variable=b,
			command=self.ShowTooltipNumberPressed)
		c.grid(row=1,column=0,columnspan=2,pady=(0,5),sticky='W')
		ToolTip(c,2000)

		# You can just pass a text string to the ToolTip
		l = ttk.Label(f,text='Tooltip show delay:')
		l.grid(row=2,column=0,sticky='W')
		ToolTip(l,"Tooltip text for the label 'Tooltip show delay' passed directly" \
					 " in the ToolTip constructor.")

		# To have the tooltip call a function in your code when it needs
		# a new tooltip, create the ToolTip and pass a function using
		# ToolTip(widget,msgFunc=self.CallbackFunctionName)
		# We'll apply this type of ToolTip to the Slider.
		s = ttk.Scale(f,from_=0,to=5.0,
			command=self.TooltipDelaySliderChanged,orient='horizontal',length=75)
		s.grid(row=2,column=1,sticky='W')
		# This is a static variable, so you must reference it by module name
		s.set(ToolTip.ShowTipDelay)	# Set to the default value of 1.0 sec
		ToolTip(s,msgFunc=self.SampleTooltipCallback)

	def PressMe ( self ):
		print ("Pressed")
	def ShowTooltipNumberPressed ( self ):
		# This is a static variable, so you must reference it by module name
		ToolTip.ShowTipNumber = not ToolTip.ShowTipNumber
	def HideTooltipsPressed ( self ):
		# This is a static variable, so you must reference it by module name
		ToolTip.ShowToolTips = not ToolTip.ShowToolTips
	def TooltipDelaySliderChanged ( self, val ):
		# This is a static variable, so you must reference it by module name
		ToolTip.ShowTipDelay = float(val)
	def SampleTooltipCallback ( self ):
		# Format and return a ToolTip string. This provides a method of
		# dynamically changing a ToolTip based on the current program state
		text = "This is a sample tooltip returned by the callback function" \
			"'SampleTooltipCallback'.\n\n" \
			"The current time is %s\n\n" \
			"The slider value is %.2f sec" % \
			(datetime.datetime.now().strftime("%H:%M:%S"),ToolTip.ShowTipDelay)
		return text

if __name__ == '__main__':
	win = Tk()
	Style().theme_use('clam')	# I like this theme, so sue me.
	win.minsize(400,250)
	app = TooltipTest(win,title="Tooltip Test Application")
	win.mainloop()
