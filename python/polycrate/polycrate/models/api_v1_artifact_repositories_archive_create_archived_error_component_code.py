from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_repositories_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
