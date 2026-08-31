from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_artifact_repositories_archive_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
