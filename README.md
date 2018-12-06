# XnapBoxDataGrabberPy
XnapBox Data Grabber in Python

## Getting Started
This is a Python example of grabbing data from XnapBox. You can collect the face image and metadata. 

## Prerequisites
Python 2.7+ and twisted
```
sudo pip install twisted[tls]
```

## XnapBox (Image) HTTP Headers (>= r.2.4.0)
```
X-Timestamp:YYYYMMDDTHHMMSS-SSSSSSSSSSS.MMMMMM-FFFFFFFF
YYYYMMDD=Year,Month,Day (XnapBox local time, recommend to configure timesync with NTP/ONVIF)
HHMMSS=Hour,Minutes,Seconds (XnapBox local time, recommend to configure timesync with NTP/ONVIF)
SSSSSSSSSSS=stream time in seconds portion (per session)
MMMMMM=stream time in micro seconds portion (per session)
FFFFFFFF=frame no/count (per session)

X-CaptureTime: 999999999
Epoch (UNIX) time of frame capture

X-SourceID: 9
Channel number of multiple channel XB. Start from zero.

X-FrameNo: 999
Frambe number of captured frame. Reset when rtsp connection restart.

X-objectYpos:
(Y Coordinate of Object/Face Centroid in the whole frame, integer: 0-1200)

X-objectXpos: 9999
(X Coordinate of Object/Face Centroid in the whole frame, integer: 0-2000)
 
X-objectWidth: 9999
(Face Width in XB Face, integer: 72-1200)

X-objectHeight: 9999 (Face Height in XB Face)
(Image width & height in Object, Face Width & Height in XB Face, integer: 72-1200)
 
X-TrackerID: 99999999
(Integer from 0-99999999, back to 0 after 99999999)
 
X-TrackDir: (obsoleted)
 
X-ObjectColor1HSV: #999#999#999
(Dominant Color, H, integer: 0-360, S, integer: 0-100%, V, integer: 0-100%)
X-ObjectColor2HSV: #999#999#999
(2nd Dominant Color, H, integer: 0-360, S, integer: 0-100%, V, integer: 0-100%)

X-BlurIndex: 99999
(Blur index indicate the blur level: 0-10000. Normally >75 means sharp)
```

## XnapBox (Heartbeat) HTTP Headers (>= r.2.4.0)
```
X-CaptureTime: 999999999
Epoch (UNIX) time of heartbeat generate.
You may use this heartbeat to check whether time is synchronized and connection a fine.
```

## XnapBox HTTP Headers (>= r.0.9.8)
```
X-Timestamp:YYYYMMDDTHHMMSS-SSSSSSSSSSS.MMMMMM-FFFFFFFF
YYYYMMDD=Year,Month,Day (XnapBox local time, recommend to configure timesync with NTP/ONVIF)
HHMMSS=Hour,Minutes,Seconds (XnapBox local time, recommend to configure timesync with NTP/ONVIF)
SSSSSSSSSSS=stream time in seconds portion (per session)
MMMMMM=stream time in micro seconds portion (per session)
FFFFFFFF=frame no/count (per session)

X-objectYpos:
(Y Coordinate of Object/Face Centroid in the whole frame, integer: 0-1200)

X-objectXpos: 9999
(X Coordinate of Object/Face Centroid in the whole frame, integer: 0-2000)
 
X-objectWidth: 9999
(Face Width in XB Face, integer: 72-1200)

X-objectHeight: 9999 (Face Height in XB Face)
(Image width & height in Object, Face Width & Height in XB Face, integer: 72-1200)
 
X-TrackerID: 99999999
(Integer from 0-99999999, back to 0 after 99999999)
 
X-TrackDir: (obsoleted)
 
X-ObjectColor1HSV: #999#999#999
(Dominant Color, H, integer: 0-360, S, integer: 0-100%, V, integer: 0-100%)
X-ObjectColor2HSV: #999#999#999
(2nd Dominant Color, H, integer: 0-360, S, integer: 0-100%, V, integer: 0-100%)

X-BlurIndex: 99999
(Blur index indicate the blur level: 0-10000. Normally >75 means sharp)
```

## Authors

Original author: Sergey Lalov

Original source code can be found at [Google code][origin].

The original source code was adopted and fixed by Xnap Development Team in 2017

## License

This software is licensed under [GNU General Public License][GNU GPL] and distributed AS IS, without warranties of any kind.

[GNU GPL]: http://opensource.org/licenses/gpl-3.0.html "GNU General Public License text"
[origin]: http://code.google.com/p/python-mjpeg-over-http-client/ "Original project page"
