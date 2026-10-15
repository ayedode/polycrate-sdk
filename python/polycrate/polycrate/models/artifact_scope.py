from typing import Literal

ArtifactScope = Literal["system", "user"]

ARTIFACT_SCOPE_VALUES: set[ArtifactScope] = {
    "system",
    "user",
}


def check_artifact_scope(value: str) -> ArtifactScope:
    if value in ARTIFACT_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_SCOPE_VALUES!r}")
