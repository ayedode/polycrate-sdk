from typing import Literal

ApiV1ArtifactRepositoriesCreateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_artifact_repositories_create_kind_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateKindErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
