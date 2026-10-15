from typing import Literal

ArtifactRegistryRequestKind = Literal["harbor"]

ARTIFACT_REGISTRY_REQUEST_KIND_VALUES: set[ArtifactRegistryRequestKind] = {
    "harbor",
}


def check_artifact_registry_request_kind(value: str) -> ArtifactRegistryRequestKind:
    if value in ARTIFACT_REGISTRY_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_REQUEST_KIND_VALUES!r}")
