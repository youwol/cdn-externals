from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import PackageType, Dependencies, Template, RunTimeDeps
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template

# after build:
#   grapes/grapes.min.js: use youwol cdn url to fetch fontawesome icons (search for 'fontawesome')
#   replace :
#     https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/ by
#     /api/assets-gateway/raw/package/Zm9udGF3ZXNvbWU=/5.12.1/


template = Template(
    path=Path(__file__).parent,
    type=PackageType.Library,
    name="grapesjs",
    exportedSymbol="grapesjs",
    version="0.18.3",
    author="greinisch@youwol.com"
)

generate_template(template)
