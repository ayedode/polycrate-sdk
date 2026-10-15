from typing import Literal

ArtifactRepositoryScope = Literal["system", "user"]

ARTIFACT_REPOSITORY_SCOPE_VALUES: set[ArtifactRepositoryScope] = {
    "system",
    "user",
}


def check_artifact_repository_scope(value: str) -> ArtifactRepositoryScope:
    if value in ARTIFACT_REPOSITORY_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_SCOPE_VALUES!r}")
