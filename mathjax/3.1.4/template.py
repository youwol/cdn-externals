from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

#  package.json.main point to text-mml-chtml.js, this is the original except
#    in text-mml-chtml -> replace:
#      u.src=u.src.replace(/%%URL%%/,r) by
#      u.src=u.src.replace(/%%URL%%/,'/api/assets-gateway/raw/package/bWF0aGpheA==/3.1.4/fonts';
#    Need a proper installation of mathjax

template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="mathjax",
    exportedSymbol="Mathjax",
    version="3.1.4",
    author="greinisch@youwol.com"
)

generate_template(template)
