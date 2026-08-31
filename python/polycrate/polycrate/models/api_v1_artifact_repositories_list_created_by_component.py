from typing import Literal

ApiV1ArtifactRepositoriesListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_ARTIFACT_REPOSITORIES_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1ArtifactRepositoriesListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_artifact_repositories_list_created_by_component(
    value: str,
) -> ApiV1ArtifactRepositoriesListCreatedByComponent:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
