from typing import Literal

ArtifactRepositoryState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_REPOSITORY_STATE_VALUES: set[ArtifactRepositoryState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_repository_state(value: str) -> ArtifactRepositoryState:
    if value in ARTIFACT_REPOSITORY_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_STATE_VALUES!r}")
