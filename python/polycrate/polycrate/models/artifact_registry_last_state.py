from typing import Literal

ArtifactRegistryLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_REGISTRY_LAST_STATE_VALUES: set[ArtifactRegistryLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_registry_last_state(value: str) -> ArtifactRegistryLastState:
    if value in ARTIFACT_REGISTRY_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_LAST_STATE_VALUES!r}")
