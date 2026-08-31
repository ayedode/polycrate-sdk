from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_artifact_repositories_archive_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
