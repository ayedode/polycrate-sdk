from typing import Literal

ArtifactPackageLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_PACKAGE_LAST_STATE_VALUES: set[ArtifactPackageLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_package_last_state(value: str) -> ArtifactPackageLastState:
    if value in ARTIFACT_PACKAGE_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_LAST_STATE_VALUES!r}")
