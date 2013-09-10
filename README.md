imgproc-pygame
==============

# What is this?

There is an very helpful image processing tutorial for use with the Raspberry Pi [here](http://www.cl.cam.ac.uk/freshers/raspberrypi/tutorials/image-processing/) and [here _newer?_](http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/image_processing/). Unfortunately the python examples depend on a provided C library which depends on Linux header files which may not be availiable on say - OS X where you might also like to do some image processing.

To that end this is a rewrite of the imgproc.py script to use pygame rather than the C library as a drop-in replacement, the example scripts from the [original zip](http://www.cl.cam.ac.uk/downloads/freshers/image_processing.tar.gz) should run without modification. ([file an issue](https://github.com/jake5991/imgproc-pygame/issues) if this is not the case!).

### Release Notes
###### Updated: 10/09/2013
+ Running make builds extension with cython.
+ A new setup.py script.
###### Old
+ Current version contains a hasty workaround for pygames's surface locking which slows down processing.

#### Requirements

`make`, `Python 2.7`, `pygame` and optionally `cython`.

#### Installation

##### One-liner
Note: You may be prompted for a super-user password.

```sh
wget https://github.com/jake5991/imgproc-pygame/archive/master.zip && unzip master.zip && make
```

If you use either of the methods that use `make` your python packages folder will be detected automatically. You can see this location by running `make location`.

##### Manual
###### Pure Python

Follow these instructions if you cannot compile C programs.

+ [Download the Zip](https://github.com/jake5991/imgproc-pygame/archive/master.zip)
+ Unzip it!
+ Move imgproc.py to your site-packages or dist-files folder (Python installation dependant).

or run `make install-pure`.

###### Cython (faster)

+ [Download the Zip](https://github.com/jake5991/imgproc-pygame/archive/master.zip)
+ Unzip it!
+ `cd` to the unzipped folder.
+ Run `make`.

or run `python setup.py build_ext --inplace` to produce `imgproc.c` and `imgproc.so` in the current directory.

Check the [makefile](https://github.com/jake5991/imgproc-pygame/blob/master/makefile) for more options.

### FAQ

I dont have pygame installed?
_Run `make install-pygame` from the unzipped imgproc-pygame folder or see the [pygame install pages](http://www.pygame.org/install.html) for binary files._

I dont have cython installed?
_Run `make install-cython` from the unzipped imgproc-pygame folder or see the [pygame install pages](http://www.pygame.org/install.html) for binary files._

It isn't working...?
_Please [file an issue](https://github.com/jake5991/imgproc-pygame/issues) with your exact problem.

How can I contribute?
_[Pull requests welcome](https://github.com/jake5991/imgproc-pygame/pulls)._

# License

Copyright (C) 2012 Jake Burton

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
