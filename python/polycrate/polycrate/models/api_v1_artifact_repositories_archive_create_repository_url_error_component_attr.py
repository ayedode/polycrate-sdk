from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponentAttr = Literal["repository_url"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponentAttr
] = {
    "repository_url",
}


def check_api_v1_artifact_repositories_archive_create_repository_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
