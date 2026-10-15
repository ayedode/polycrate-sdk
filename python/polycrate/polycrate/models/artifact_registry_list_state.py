from typing import Literal

ArtifactRegistryListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_REGISTRY_LIST_STATE_VALUES: set[ArtifactRegistryListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_registry_list_state(value: str) -> ArtifactRegistryListState:
    if value in ARTIFACT_REGISTRY_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_LIST_STATE_VALUES!r}")
