from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_artifact_repositories_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
