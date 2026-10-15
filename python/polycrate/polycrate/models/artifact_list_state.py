from typing import Literal

ArtifactListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_LIST_STATE_VALUES: set[ArtifactListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_list_state(value: str) -> ArtifactListState:
    if value in ARTIFACT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_LIST_STATE_VALUES!r}")
