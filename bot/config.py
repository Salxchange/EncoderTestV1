#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = int("7324525")
    API_HASH = ("d28604398dc13af15dd108bb34a27a54")
    BOT_TOKEN = ("6509653210:AAEap5ed7KpIh-6Ym679jZzNcAhYORvHJ_k")
    DEV = 5467555331
    OWNER = ("1966867320")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By AnshuSharma (https://github.com/Anshusharma75/TG-videoCompress)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMB = ("https://graph.org/file/0b762a5819c0edc8e6da4.jpg")
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit(1)
