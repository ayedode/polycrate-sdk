from typing import Literal

ArtifactState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_STATE_VALUES: set[ArtifactState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_state(value: str) -> ArtifactState:
    if value in ARTIFACT_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_STATE_VALUES!r}")
