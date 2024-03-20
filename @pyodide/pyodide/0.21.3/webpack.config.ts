const apiVersion = "021";
const externals = {};
const path = require("path");
require("webpack");
const pkg = require("./package.json");
const ROOT = path.resolve(__dirname, "src");
const DESTINATION = path.resolve(__dirname, "full");
const { BundleAnalyzerPlugin } = require("webpack-bundle-analyzer");

module.exports = {
  context: ROOT,
  resolve: {
    modules: [ROOT, "node_modules"],
    fallback: {
      url: require.resolve("url/"),
      fs: false,
      tls: false,
      net: false,
      path: false,
      zlib: false,
      http: false,
      https: false,
      stream: false,
      crypto: false,
      "crypto-browserify": require.resolve("crypto-browserify"), //if you want to use this module also don't forget npm i crypto-browserify
    },
  },
  entry: {
    main: "./index.ts",
  },
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: "static",
      reportFilename: "./bundle-analysis.html",
      openAnalyzer: false,
    }),
  ],
  output: {
    path: DESTINATION,
    publicPath: `/api/assets-gateway/raw/package/cHlvZGlkZQ==/0.21.3/full/`,
    libraryTarget: "umd",
    umdNamedDefine: true,
    library: `${pkg.name}_APIv${apiVersion}`,
    filename: pkg.name + ".js",
    globalObject: `(typeof self !== 'undefined' ? self : this)`,
  },
  externals,
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: [{ loader: "ts-loader" }],
        exclude: /node_modules/,
      },
    ],
  },
  devtool: "source-map",
};
