from typing import Literal

ArtifactRepositoryListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_REPOSITORY_LIST_STATE_VALUES: set[ArtifactRepositoryListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_repository_list_state(value: str) -> ArtifactRepositoryListState:
    if value in ARTIFACT_REPOSITORY_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_LIST_STATE_VALUES!r}")
