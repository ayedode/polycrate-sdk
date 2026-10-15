from typing import Literal

ArtifactRequestScope = Literal["system", "user"]

ARTIFACT_REQUEST_SCOPE_VALUES: set[ArtifactRequestScope] = {
    "system",
    "user",
}


def check_artifact_request_scope(value: str) -> ArtifactRequestScope:
    if value in ARTIFACT_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REQUEST_SCOPE_VALUES!r}")
