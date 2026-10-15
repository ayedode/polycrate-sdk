from typing import Literal

ArtifactPackageScope = Literal["system", "user"]

ARTIFACT_PACKAGE_SCOPE_VALUES: set[ArtifactPackageScope] = {
    "system",
    "user",
}


def check_artifact_package_scope(value: str) -> ArtifactPackageScope:
    if value in ARTIFACT_PACKAGE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_SCOPE_VALUES!r}")
