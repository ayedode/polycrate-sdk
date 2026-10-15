from typing import Literal

ArtifactPackageListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_PACKAGE_LIST_STATE_VALUES: set[ArtifactPackageListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_package_list_state(value: str) -> ArtifactPackageListState:
    if value in ARTIFACT_PACKAGE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_LIST_STATE_VALUES!r}")
