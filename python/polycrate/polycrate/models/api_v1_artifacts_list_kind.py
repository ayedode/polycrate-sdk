from typing import Literal

ApiV1ArtifactsListKind = Literal["docker", "helm", "oci", "polycrate", "source"]

API_V1_ARTIFACTS_LIST_KIND_VALUES: set[ApiV1ArtifactsListKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_api_v1_artifacts_list_kind(value: str) -> ApiV1ArtifactsListKind:
    if value in API_V1_ARTIFACTS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_LIST_KIND_VALUES!r}")
