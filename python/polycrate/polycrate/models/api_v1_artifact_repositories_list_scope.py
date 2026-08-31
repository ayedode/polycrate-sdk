from typing import Literal

ApiV1ArtifactRepositoriesListScope = Literal["system", "user"]

API_V1_ARTIFACT_REPOSITORIES_LIST_SCOPE_VALUES: set[ApiV1ArtifactRepositoriesListScope] = {
    "system",
    "user",
}


def check_api_v1_artifact_repositories_list_scope(value: str) -> ApiV1ArtifactRepositoriesListScope:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_SCOPE_VALUES!r}")
