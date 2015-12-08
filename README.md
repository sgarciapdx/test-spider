# test-spider

This spider is set up to work with the VMs provided in the scrapy-vagrant repo. The web VM in that
repo should have an xkcd archive set up in `/vagrant/web/html`. This spider is set up to begin from
the most recent page contained in the archive and continually scrape the pages pointed to by the
'Previous' links until it reaches the end of the archive.

# Setup & usage

* Clone this repo into your `scrapy-vagrant` directory
* Start your scrapy and web VMs
* SSH into your scrapy VM
* Navigate to the directory containing this README
* Run `scrapy crawl xkcd`

# Configuration

Configurations for this spider can be found in [`xkcd_test/settings.py`](https://github.com/sgarciapdx/test-spider/blob/master/xkcd_test/settings.py). If you take a look there,
you'll see there are comments near the end of the file about how to play with configs for
`HTTPCacheMiddleware`.
