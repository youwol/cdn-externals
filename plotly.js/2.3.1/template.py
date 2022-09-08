from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

# Be careful: need to add the following to webpack.config:
#     *  in resolve : fallback: { stream: require.resolve("stream-browserify") },
#     *  in plugins : new webpack.DefinePlugin({
#          "process.env.NODE_DEBUG": JSON.stringify(process.env.NODE_DEBUG),
#        }),
template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="plotly.js",
    exportedSymbol="Plotly",
    version="2.3.1",
    author="greinisch@youwol.com",
    dependencies=Dependencies(
        devTime={
            #  If not included => error during yarn build
            "buffer": "^6.0.3",
            "assert": "^2.0.0",
            "stream-browserify": "^3.0.0",
        }
    )
)

generate_template(template)
