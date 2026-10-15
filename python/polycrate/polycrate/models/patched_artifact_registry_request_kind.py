from typing import Literal

PatchedArtifactRegistryRequestKind = Literal["harbor"]

PATCHED_ARTIFACT_REGISTRY_REQUEST_KIND_VALUES: set[PatchedArtifactRegistryRequestKind] = {
    "harbor",
}


def check_patched_artifact_registry_request_kind(value: str) -> PatchedArtifactRegistryRequestKind:
    if value in PATCHED_ARTIFACT_REGISTRY_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ARTIFACT_REGISTRY_REQUEST_KIND_VALUES!r}")
