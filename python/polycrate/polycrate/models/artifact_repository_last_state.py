from typing import Literal

ArtifactRepositoryLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_REPOSITORY_LAST_STATE_VALUES: set[ArtifactRepositoryLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_repository_last_state(value: str) -> ArtifactRepositoryLastState:
    if value in ARTIFACT_REPOSITORY_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_LAST_STATE_VALUES!r}")
