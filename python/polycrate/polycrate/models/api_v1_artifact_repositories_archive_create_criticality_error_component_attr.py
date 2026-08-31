from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_artifact_repositories_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
