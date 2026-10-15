from typing import Literal

PatchedArtifactRequestKind = Literal["docker", "helm", "oci", "polycrate", "source"]

PATCHED_ARTIFACT_REQUEST_KIND_VALUES: set[PatchedArtifactRequestKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_patched_artifact_request_kind(value: str) -> PatchedArtifactRequestKind:
    if value in PATCHED_ARTIFACT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ARTIFACT_REQUEST_KIND_VALUES!r}")
