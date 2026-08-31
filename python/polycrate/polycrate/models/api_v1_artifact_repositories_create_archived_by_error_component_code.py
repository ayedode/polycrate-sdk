from typing import Literal

ApiV1ArtifactRepositoriesCreateArchivedByErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesCreateArchivedByErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_artifact_repositories_create_archived_by_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateArchivedByErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
