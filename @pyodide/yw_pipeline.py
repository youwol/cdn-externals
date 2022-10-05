from typing import List

from pydantic import BaseModel
from youwol.environment.models_project import Artifact, Flow, Pipeline, PipelineStep, FileListing, JsBundle
from youwol.pipelines.pipeline_typescript_weback_npm import PublishCdnLocalStep, create_sub_pipelines_publish_cdn
from youwol_utils.context import Context
from youwol_utils.utils_paths import parse_json


class BuildStep(PipelineStep):
    id: str = "build"
    run: str = "echo 'Nothing to do'"
    sources: FileListing = FileListing(
        include=["*", "full/**"],
        ignore=['.yw_pipeline/**']
    )

    artifacts: List[Artifact] = [
        Artifact(
            id='dist',
            files=FileListing(
                include=["*", "full/**"],
                ignore=['.yw_pipeline/**', 'cdn.zip']
            )
        )
    ]


class PipelineConfig(BaseModel):
    target: JsBundle = JsBundle()


async def pipeline(context: Context) -> Pipeline:

    steps, dags = await create_sub_pipelines_publish_cdn(start_step="cdn-local", context=context)

    return Pipeline(
        target=JsBundle(),
        tags=["javascript", "library", "npm", "pyodide", "external"],
        projectName=lambda path:  parse_json(path / "package.json")["name"],
        projectVersion=lambda path: parse_json(path / "package.json")["version"],
        steps=[
            BuildStep(),
            PublishCdnLocalStep(packagedArtifacts=['dist']),
            *steps
        ],
        flows=[
            Flow(
                name="prod",
                dag=[
                    "build > cdn-local",
                    *dags
                ]
            )
        ]
    )
