from typing import Literal

ArtifactRequestKind = Literal["docker", "helm", "oci", "polycrate", "source"]

ARTIFACT_REQUEST_KIND_VALUES: set[ArtifactRequestKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_artifact_request_kind(value: str) -> ArtifactRequestKind:
    if value in ARTIFACT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_REQUEST_KIND_VALUES!r}")
