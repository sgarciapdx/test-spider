# test-spider

This spider is set up to work with the VMs provided in the scrapy-vagrant repo. The web VM in that
repo should have an xkcd archive set up in `/vagrant/web/html`. This spider is set up to begin from
the most recent page contained in the archive and continually scrape the pages pointed to by the
'Previous' links until it reaches the end of the archive.

# First-time setup
If you haven't already, clone the [scrapy-vagrant](https://github.com/PDX-Capstone-Team-C/scrapy-vagrant) repo and follow 
the setup instructions there. If you've cloned it but haven't touched it in a while, pull it so you're up to date. Things
may have changed recently, so make sure to look at the README for details.

On your local machine:
* `cd /path/to/scrapy-vagrant`
* `cp /path/to/[xkcd archive] web`
* `vagrant up web`
* `vagrant ssh web`

In the web VM:
* `cd /vagrant/web`
* `tar zxvf [xkcd archive]`

This will place the files in the archive in `/vagrant/web/html`, exactly where they need to be. 

If you follow these directions, the last part will place the contents of the archive in `/vagrant/web/html`

# Usage
* `cd /path/to/scrapy-vagrant`
* `vagrant up scrapy-vm web`
* `vagrant ssh scrapy-vm`
* `cd /vagrant/scrapy-vagrant/test-spider`
* `scrapy crawl xkcd`

This will start the spider, and you can watch it do its work. The cache will be saved in the `.scrapy` subdirectory
under different subdirectories depending on the config options.

# Configuration

Configurations for this spider can be found in [`xkcd_test/settings.py`](https://github.com/sgarciapdx/test-spider/blob/master/xkcd_test/settings.py). If you take a
look there, you'll see there are comments near the end of the file about how to play with configs for `HTTPCacheMiddleware`.
