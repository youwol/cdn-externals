import re
import shutil
from pathlib import Path

from youwol.pipelines.pipeline_typescript_weback_npm import Template, PackageType, Dependencies, \
    RunTimeDeps, Bundles, MainModule
from youwol.pipelines.pipeline_typescript_weback_npm.external import generate_template
from youwol.utils import parse_json

folder_path = Path(__file__).parent

pkg_json = parse_json(folder_path / 'package.json')

css_path = folder_path / 'node_modules' / 'bootstrap-select' / 'dist' / 'css'

externals_deps = {
    "bootstrap": "^4.0.0",
    "jquery": "^3.6.1"
}
in_bundle_deps = {
    "bootstrap-select": pkg_json['version']
}
dev_deps = {
    "cpx": "^1.5.0"
}

template = Template(
    path=folder_path,
    type=PackageType.LIBRARY,
    name=pkg_json['name'],
    version=pkg_json['version'],
    shortDescription=pkg_json['description'],
    author=pkg_json['author'],
    dependencies=Dependencies(
        runTime=RunTimeDeps(
            externals=externals_deps,
            includedInBundle=in_bundle_deps
        ),
        devTime=dev_deps
    ),
    bundles=Bundles(
        mainModule=MainModule(
            entryFile='./index.ts',
            loadDependencies=list(externals_deps.keys()),
            aliases=[]
        )
    ),
    inPackageJson={
        "scripts": {
            # Below are regular scripts
            **pkg_json['scripts'],
            "build:dev": "yarn pre-build && yarn copy-css && webpack --mode development",
            "build:prod": "yarn pre-build && yarn copy-css && webpack --mode production",
            "copy-css": f"cpx \"{css_path}/*\" \"./\"",
        }
    },
    userGuide=True
)

generate_template(template)
shutil.copyfile(
    src=folder_path / '.template' / 'src' / 'auto-generated.ts',
    dst=folder_path / 'src' / 'auto-generated.ts'
)
for file in ['README.md',
             # '.gitignore',
             '.npmignore', '.prettierignore', 'LICENSE', 'package.json',
             'tsconfig.json', 'jest.config.ts', 'webpack.config.ts']:
    shutil.copyfile(
        src=folder_path / '.template' / file,
        dst=folder_path / file
    )

# Fix imports of jquery

# File path to the file you want to modify
file_path = folder_path / 'src' / 'auto-generated.ts'

# Read the file content
with open(file_path, 'r') as file:
    content = file.read()

pattern = r'"jquery_APIv\d+"'
replacement = lambda match: f'[{match.group(0)}, "default"]'
new_content = re.sub(pattern, replacement, content)

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.write(new_content)