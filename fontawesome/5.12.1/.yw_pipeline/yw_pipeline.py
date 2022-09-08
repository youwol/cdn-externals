from typing import List
from youwol.environment.forward_declaration import YouwolEnvironment
from youwol.environment.models import IPipelineFactory
from youwol.environment.models_project import Artifact, Flow, Pipeline, PipelineStep, FileListing, JsBundle
from youwol.pipelines.pipeline_typescript_weback_npm import PublishCdnRemoteStep, PublishCdnLocalStep
from youwol_utils.context import Context
from youwol_utils.utils_paths import parse_json


class BuildStep(PipelineStep):
    id: str = "build"
    run: str = "echo 'Nothing to do'"
    sources: FileListing = FileListing(
        include=["*", "**"],
        ignore=['.yw_pipeline/**', 'cdn.zip', 'node_modules/**']
    )

    artifacts: List[Artifact] = [
        Artifact(
            id='dist',
            files=FileListing(
                include=["*", "**"],
                ignore=['.yw_pipeline/**', 'cdn.zip', 'node_modules']
            )
        )
    ]


class PipelineFactory(IPipelineFactory):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def get(self, _env: YouwolEnvironment, _ctx: Context):

        return Pipeline(
            target=JsBundle(),
            tags=["javascript", "library", "npm", "external"],
            projectName=lambda path: parse_json(path / "package.json")["name"],
            projectVersion=lambda path: parse_json(path / "package.json")["version"],
            steps=[
                BuildStep(),
                PublishCdnLocalStep(packagedArtifacts=['dist']),
                PublishCdnRemoteStep()
            ],
            flows=[
                Flow(
                    name="prod",
                    dag=[
                        "build > publish-local > publish-remote "
                    ]
                )
            ]
        )
