from typing import Literal

ApiV1ArtifactRepositoriesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_repositories_create_tolerations_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateTolerationsErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
