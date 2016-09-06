# astroph_suggestions

This is the source code for the astro ph [suggestions site](http://astronomy.swin.edu.au/~soslowski/astroph/) hosted at the [Centre for Astrophysics and Supercomputing](http://astronomy.swin.edu.au/), [Swinburne University of Technology](http://www.swinburne.edu.au/). This site is providing suggestions for papers to discuss at a journal club.

It works by parsing the news feeds from Nature News & Comment, phys.org featured news, Astrobites, as well as the most read/cited astro/all papers published in the last 3 months. The news are updated daily whereas the papers weekly, see crontable. The results are stored in simple sqlite databases.

Server-side I use php to read the databases and displayed the requested type of suggestions.

## dependencies

The server it's running on provides python 2.6 and thus a [modified version](https://github.com/sosl/ads) of the ads python interface is required. If your server provides python 2.7 then you can use the [standard version](https://github.com/andycasey/ads) of the interface.
