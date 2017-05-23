#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################################################
#
# VidCutter - media cutter & joiner
#
# copyright © 2017 Pete Alexandrou
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################


from PyQt5.QtCore import pyqtSignal, QThread

from vidcutter.libs.videoservice import VideoService


class TimelineThumbsThread(QThread):
    errorOccurred = pyqtSignal(str)
    completed = pyqtSignal(list)

    def __init__(self, source: str, index: list):
        QThread.__init__(self)
        self.source = source
        self.index = index
        self.service = VideoService(self)
        self.thumbs = list()

    def __del__(self) -> None:
        self.wait()

    def generateThumbnails(self) -> None:
        status = True
        for frametime in self.index:
            self.thumbs.append(self.service.capture(self.source, frametime, VideoService.ThumbSize.TIMELINE))
        self.completed.emit(self.thumbs)

    def run(self) -> None:
        self.generateThumbnails()
