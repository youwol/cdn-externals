# Tikzjax

Coming from https://github.com/kisonecat/tikzjax.
Thanks to Jim Fowler for doing all of this.

The script dist/tikzjax.js has been 'patched' (more 'hacked') to allow:
*  use in youwol (url has been rewritten)
*  concurrent parse  (stuffs with 'setIntervall': make sure 2 'parse' are not executing at the same time)

The script 'fetch_fonts' allow to gather the fonts required by the package.

# Limitation

It is working quite OK, but packages & libraries of tikz can not be used.
To go beyond, this seems to have done the job done:

*  https://github.com/drgrice1/tikzjax/tree/ww-modifications#building
*  https://github.com/kisonecat/tikzjax/issues/2