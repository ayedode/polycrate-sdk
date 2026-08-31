from typing import Literal

ApiV1ArtifactRepositoriesListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACT_REPOSITORIES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_artifact_repositories_list_state_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesListStateErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
