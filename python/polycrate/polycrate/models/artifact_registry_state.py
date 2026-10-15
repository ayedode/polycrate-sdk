from typing import Literal

ArtifactRegistryState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_REGISTRY_STATE_VALUES: set[ArtifactRegistryState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_registry_state(value: str) -> ArtifactRegistryState:
    if value in ARTIFACT_REGISTRY_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_STATE_VALUES!r}")
