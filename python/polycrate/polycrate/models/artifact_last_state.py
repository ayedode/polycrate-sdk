from typing import Literal

ArtifactLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_LAST_STATE_VALUES: set[ArtifactLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_last_state(value: str) -> ArtifactLastState:
    if value in ARTIFACT_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_LAST_STATE_VALUES!r}")
