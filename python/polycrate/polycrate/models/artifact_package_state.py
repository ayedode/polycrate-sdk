from typing import Literal

ArtifactPackageState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ARTIFACT_PACKAGE_STATE_VALUES: set[ArtifactPackageState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_artifact_package_state(value: str) -> ArtifactPackageState:
    if value in ARTIFACT_PACKAGE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_STATE_VALUES!r}")
