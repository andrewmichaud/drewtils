drewtilities
=============

| |BSD3 License|

| |Build Status|

| |Coverage Status|

| |Issue Count|

.. image:: https://badge.fury.io/py/puckfetcher.svg
    :target: https://badge.fury.io/py/puckfetcher

.. image:: https://badge.waffle.io/alixnovosi/puckfetcher.png?label=ready&title=Ready
    :target: https://waffle.io/alixnovosi/puckfetcher
    :alt: 'Stories in Ready'

.. |BSD3 License| image:: http://img.shields.io/badge/license-BSD3-brightgreen.svg
   :target: https://tldrlegal.com/license/bsd-3-clause-license-%28revised%29
.. |Build Status| image:: https://travis-ci.org/alixnovosi/puckfetcher.svg?branch=master
   :target: https://travis-ci.org/alixnovosi/puckfetcher
.. |Coverage Status| image:: https://coveralls.io/repos/alixnovosi/puckfetcher/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/alixnovosi/puckfetcher?branch=master
.. |Issue Count| image:: https://codeclimate.com/github/alixnovosi/puckfetcher/badges/issue_count.svg
   :target: https://codeclimate.com/github/alixnovosi/puckfetcher

=====
short
=====
Utility functions, created by Drew, for Drew.
Used in `botskeleton`_ (and all the bots that use it) and `puckfetcher`_.

.. _botskeleton: https://github.com/alixnovosi/botskeleton
.. _puckfetcher: https://github.com/alixnovosi/puckfetcher

====
long
====
These are in the order defined in :code:`drewtilities.py`,
which in turn is basically defined by order of creation.
Not really organized nicely,
sorry.

=======
Methods
=======

-----------------------------
:code:`ensure_dir(directory)`
-----------------------------
Create directory if it doesn't exist.

-------------------------
:code:`expand(directory)`
-------------------------
Expand :code:`~` to :code:`$HOME`,
and expand other environment variables to their values,
in the provided path.
Designed for UNIX-based platforms:
unclear what will happen on others.

-----------------------------------------------------------------
:code:`generate_downloader(self, headers, args, max_per_hour=30)`
-----------------------------------------------------------------
Produce a callable downloader.
Provide headers for URL call,
and provide some args
(for the rate limiting
(see that later in the document)),
which will be used to identify this function in rate-limiting.
:code:`max_per_hour` is optional:
use it to decide how many times per hour downloads can happen.
The default is 30 times per hour.
The returned downloader is called as follows:
.. code-block:: python

    self.downloader(url=url, dest=dest)

where :code:`url` is where to download FROM and :code:`dest` is where to SAVE the file.
It will make the directory for the file if it does not exist.
A text progress bar is shown during download,
and while rate limit is blocking.

-----------------------------
:code:`max_clamp(val, limit)`
-----------------------------
Return :code:`val` if it is less than :code:`limit`,
otherwise return :code:`limit`.

------------------------------------
:code:`parse_int_string(int_string)`
------------------------------------
Given a string like "1 23 4-8 32 1",
return a unique list of those integers in the string,
and the integers in the ranges in the string.
For this example,
the output would be [1, 4, 5, 6, 7, 8, 23, 32].
Non-numbers ignored.
Not necessarily sorted

-----------------------------------------
:code:`rate_limited(max_per_hour, *args)`
-----------------------------------------
A decorator to rate-limit a function
(ensures that it runs no more than :code:`max_per_hour` times per hour by sleeping sometimes).
Called like this:
.. code-block:: python

    @util.rate_limited(120, name)
    def a_function(var1, var2="foo"):

--------------------------
:code:`sanitize(filename)`
--------------------------
Remove disallowed characters from potential filename.
Currently only guaranteed on Linux and OS X.
Switches "/" for "-".

-------------------------------------------------------
:code:`set_up_logging(log_filename="log", verbosity=0)`
-------------------------------------------------------
Set up a logger with reasonable settings.
Return it for log calls.

--------------------------------------------------------
:code:`random_line(file_path, encoding=FORCED_ENCODING)`
--------------------------------------------------------
At time of writing,
:code:`FORCED_ENCODING` is "UTF-8".
Refer to code for latest.
Return a line from the provided file at random.
