const apiVersion = "3";
const externals = {};
const path = require("path");
require("webpack");
const pkg = require("./package.json");
const ROOT = path.resolve(__dirname, "src");
const DESTINATION = path.resolve(__dirname, "dist");
const { BundleAnalyzerPlugin } = require("webpack-bundle-analyzer");

module.exports = {
  context: ROOT,
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
    libraryTarget: "umd",
    umdNamedDefine: true,
    library: `${pkg.name}_APIv${apiVersion}`,
    filename: pkg.name + ".js",
    globalObject: `(typeof self !== 'undefined' ? self : this)`,
  },
  resolve: {
    extensions: [".ts", "tsx", ".js"],
    modules: [ROOT, "node_modules"],
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
/*
return async ({debug}) => {
    const CDN = window['@youwol/cdn-client']
    const FluxView = window['@youwol/flux-view']
    debug('CDN', CDN)
    debug('FluxView', FluxView)
    const {chartJs} = await CDN.install({
        modules:["chart.js#^3.9.1"],
    	aliases:{'chartJs': 'chart.js_APIv3'}
    })

    console.log("tutu", Chart)
    chartJs.Chart.register(...chartJs.registerables);

    const labels = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
      ];

    const data = {
        labels: labels,
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [0, 10, 5, 2, 20, 30, 45],
        }]
    };

    const config = {
        type: 'line',
        data: data,
        options: {}
    };
    const vDOM = {
        tag:'canvas',
        width:'500',
        height:'500',
        style:{
        	width:'500px',
            height:'500px'
        },
        connectedCallback: (htmlElement) => {
            console.log('htmlElement',htmlElement)
            const myChart = new chartJs.Chart(
                htmlElement,
                config
            );
        }
    }

    debug('view', FluxView.render(vDOM))
    return true
}
 */