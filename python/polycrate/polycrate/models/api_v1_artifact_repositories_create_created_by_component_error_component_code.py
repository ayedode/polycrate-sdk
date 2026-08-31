from typing import Literal

ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_artifact_repositories_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
