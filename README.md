# Synopsis

A Python module that provides a tooltip interface for widgets in a program. The tootip text for each widget may be read from an external file, passed as a string during ToolTip construction, or dynamically created by using a user-supplied callback function.

## Motivation

This module was created as part of my efforts on the PiCameraApp, where I wanted tooltips for all the the camera controls.

## Version History

| Version    | Notes                               |
| :--------- | :----------------------------------------------------- |
| 0.1 | Initial release. Includes the files **Tooltip.py** and **Tooltips.txt**. A python test program that uses the Tooltip interfaces is also included (**ExampleTooltips.py**) |
| | |

# Installation

Download the zip file. Include the file **Tooltip.py** in your project file directory. For each file that uses Tooltips, add a **from Tooltip import .** at the begnning of the file. A sample **Tooltips.txt** file is also included that you may then modify for your use. This file may reside whereever you see fit within your project structure. See the comments at the beginning of the file for structure/layout instructions.

# Examples

The file **ExampleTooltips.py** is included which provides specific examples for including tooltips into your application.

## API Reference

The sample program **ExampleTooltips.py** has been developed using Python ver 2.7.13 and Python ver 3.5.3.

## Known Issues

| Issue      | Description / Workaround                               |
| :--------- | :----------------------------------------------------- |
| line spacing | The program loses or adds a space character on some text strings read from the file. |
| | |

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program.  If not, see http://www.gnu.org/licenses/.
