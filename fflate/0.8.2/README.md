# Wrapper of the npm package [fflate](https://www.npmjs.com/package/fflate) for publication in [WebPM](https://webpm.org).


High performance (de)compression in an 8kB package

# Installation & Build

To install the required dependencies:

```shell
yarn
```
---
To build for development:

```shell
yarn build:dev
```

To build for production:

```shell
yarn build:prod
```

# Test & Publication in WebPM

To publish the package in webpm (in local or remote environments) you should use
[py-youwol](https://l.youwol.com/doc/py-youwol) and access the project's 
pipeline through the `developer-portal` application.


Tests also require py-youwol to run on port `2001` using the configuration for integration
tests defined 
[here](https://github.com/youwol/py-youwol-configs/blob/master/test_config.py).

Then, to run the tests:

```shell
yarn test
```
