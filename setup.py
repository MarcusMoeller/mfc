#!/usr/bin/python
# -*- coding: utf-8 -*-

# With the Unity Ubuntu MindfulClock you turn your device into a Bell
# of Mindfulness.
# Concept, Design: Marcurs Möller
#                  <marcus.moeller@outlook.com>
#                  <http://apps.microsoft.com/windows/de-de/app/
#                   mindfulclock/58063160-9cc6-4dee-9d92-17df4ce4318a>
# Programming: Andreas Ulrich
#              <ulrich3110@gmail.com>,
#              <http://erasand.jimdo.com/kontakt/>
#
# This file is part of the "Unity Ubuntu MindfulClock".
# "Unity Ubuntu MindfulClock" is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# "Unity Ubuntu MindfulClock" is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See the GNU General Public License for more details. You should
# have received a copy of the GNU General Public License along with
# "Unity Ubuntu MindfulClock".
# If not, see <http://www.gnu.org/licenses/>.


from distutils.core import setup


''' Create a sourcecode distribution of Uumfc. Arguments

setup(name='NAME_SOURCE_DISTRIBUTION',
      version='TEXT',
      description='TEXT',
      long_description='TEXT',
      author='TEXT',
      author_email='TEXT',
      maintainer='TEXT',
      maintainer_email='TEXT',
      url='TEXT',
      download_url='TEXT',
      packages=['paket1', 'paket2', 'paket1.unterpaket1'],
      package_dir={'paket1': 'source/pkg1',
                   'paket2': 'source/pkg2',
                   'paket1.unterpaket1': 'source/pkg2/pkg2-1'},
      package_data={'paket1': ['datei1.txt', 'datei2.txt'],
                    'paket2': ['datei3.txt']},
      py_modules=['modul1', 'modul2']
      scripts=['script1.sh', 'script2.sh']
      data_files=[('icons', ['icons/icon1.png', 'icons/icon2.png']),
                  ('config', ['config/programm.cfg'])],
      ext_modules=,
      script_name=,
      license=,
      console=,
      window=)

'''

DESCRIPTION = '''
With the Unity Ubuntu MindFulClock you turn your device into a Bell
of Mindfulness.
'''
LONG_DESCRIPTION = '''
With the Ubuntu Unity MindFulClock you turn your device into a Bell of
Mindfulness. During the day you hear regularly the bell and it gives
you the  opportunity to pause for a moment and enjoy the present of
Mindfulness.
'''


setup(name='uumfc1',
      version='1.0.1',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author='Andreas Ulrich',
      author_email='ulrich3110@gmail.com',
      url='https://github.com/ulrich3110/uumfc.git',
      packages=['uumfc1'],
      package_data={'uumfc1': ['doku/*.html',
                               'icons/*.png',
                               'icons/16/*.png',
                               'icons/22/*.png',
                               'icons/32/*.png',
                               'locale/de/LC_MESSAGES/*.mo',
                               'pofiles/de/LC_MESSAGES/*.po',
                               'sounds/*.mp3']},
      scripts=['uumfc1run'],
      license='GPL3')