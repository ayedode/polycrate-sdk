from typing import Literal

ApiV1ArtifactRepositoriesListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_ARTIFACT_REPOSITORIES_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesListUpdatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_artifact_repositories_list_updated_at_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesListUpdatedAtErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
