from typing import Literal

ApiV1ArtifactRepositoriesListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACT_REPOSITORIES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesListKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_artifact_repositories_list_kind_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesListKindErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
