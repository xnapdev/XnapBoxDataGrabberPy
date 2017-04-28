#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name:       Python M-JPEG Over HTTP Client Program
Version:    0.1
Purpose:    This program connects to an MJPEG stream and saves retrived images.
Author:     Sergey Lalov
Date:       2011-03-30
License:    GPL
Target:     Cross Platform
Require:    Python 2.7+. Modules: zope.interface, twisted
"""
from twisted.internet import reactor

from http_mjpeg_client import MJPEGFactory

import argparse

def processImage(img, header):
    'This function is invoked by the MJPEG Client protocol'
    print 'processImage.Header: \n', header
    
    headers = header.splitlines()
    timestamp = '';
    trackerid = '';
    for line in headers:
        if (":" in line):
            lhs, rhs = line.split(":", 1)
            if lhs == 'X-Timestamp': # Connection went fine
                timestamp = rhs;
            if lhs == 'X-TrackerID':
                trackerid = rhs;
                
    if (timestamp == "000000000000000-000000000000000000000000000"):
        print 'Heartbeat'
    else:
        # Process image
        # Just save it as a file in this example
        filename = config['filename'] + '-' + trackerid + '-' + timestamp + '.jpg';
        f = open(filename, 'wb')
        f.write(img)
        f.close()
        
        print 'Image saved to ' + filename;
    
config = {
    'callback': processImage,
}

def main():
    # Retrieve configuration from command line arguments
    parser = argparse.ArgumentParser(description='Tool for grabbing frames from MJPEG over HTTP video stream to image file.')
    parser.add_argument('--request', metavar='PATH', default='/',
                        help='a path in the server to request for the videostream')
    parser.add_argument('--ip', required=True, help='XnapBox IP-address')
    parser.add_argument('--port', type=int, default=8080,
                        help='Remote server port (default: 8080)')
    parser.add_argument('--login', help='Username for authentication (optional)')
    parser.add_argument('--password', help='Password for authentication (optional)')
    parser.add_argument('--filename', default='frame', help='A file name to save frames (default: frame.jpg)')
    args = parser.parse_args()
    # Define connection parameters, login and password are optional.
    config.update(vars(args))
    # Make a connection
    print 'XnapBox DataGrabber Python'
    reactor.connectTCP(config['ip'], config['port'], MJPEGFactory(config)) #@UndefinedVariable
    reactor.run() #@UndefinedVariable
    print 'XnapBox DataGrabber Python stopped.'

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
