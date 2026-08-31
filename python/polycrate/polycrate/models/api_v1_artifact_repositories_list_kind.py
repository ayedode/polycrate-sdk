from typing import Literal

ApiV1ArtifactRepositoriesListKind = Literal["docker", "helm", "oci", "polycrate", "source"]

API_V1_ARTIFACT_REPOSITORIES_LIST_KIND_VALUES: set[ApiV1ArtifactRepositoriesListKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_api_v1_artifact_repositories_list_kind(value: str) -> ApiV1ArtifactRepositoriesListKind:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_KIND_VALUES!r}")
