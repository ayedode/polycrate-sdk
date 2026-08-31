from typing import Literal

ApiV1ArtifactRepositoriesListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ARTIFACT_REPOSITORIES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesListNameErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_artifact_repositories_list_name_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesListNameErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
