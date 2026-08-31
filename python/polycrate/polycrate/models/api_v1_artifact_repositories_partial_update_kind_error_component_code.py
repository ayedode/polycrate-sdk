from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_artifact_repositories_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateKindErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
