from typing import Literal

ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_artifact_repositories_update_created_by_component_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
