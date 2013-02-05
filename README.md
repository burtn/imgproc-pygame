imgproc-pygame
==============

# What is this?

There is an very helpful image processing tutorial for use with the Raspberry Pi [here](http://www.cl.cam.ac.uk/freshers/raspberrypi/tutorials/image-processing/) and [here _newer?_](http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/image_processing/). Unfortunately the python examples depend on a provided C library which depends on Linux header files which may not be availiable on say - OS X where you might also like to do some image processing.
To that end this is a rewrite of the imgproc.py script to use pygame rather than the C library as a drop-in replacement, the example scripts from the [original zip](http://www.cl.cam.ac.uk/downloads/freshers/image_processing.tar.gz) should run without modification. ([file an issue](https://github.com/jake5991/imgproc-pygame/issues) if this is not the case!).

### Release Notes
+ Current version contains a hasty workaround for pygames's surface locking which slows down processing.

#### Installation

###### One-liner
Note: You may be prompted for a super-user password.

```sh
wget http://dl.dropbox.com/u/4875815/imgproc/imgproc-pygame.zip && unzip imgproc-pygame.zip && make install
```

###### Manual

+ [Download the Zip](http://dl.dropbox.com/u/4875815/imgproc/imgproc-pygame.zip)
+ Unzip it!
+ Move imgproc.py to your site-packages or dist-files folder (Python installation dependant)

### FAQ

+ I dont have pygame installed?
+ _Run make install-pygame from the unzipped imgproc-pygame folder_
+ **Alternative** _See the [pygame install pages for binary files](http://www.pygame.org/install.html)_

+ It isn't working?
+ _Please [file an issue](https://github.com/jake5991/imgproc-pygame/issues) with your exact problem!_

+ Your code is /bad/slow/inefficient/etc
+ _[Pull requests welcome](https://github.com/jake5991/imgproc-pygame/pulls)!_

# License

Copyright (C) 2012 Jake Burton

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
