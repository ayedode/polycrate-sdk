from typing import Literal

ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_artifact_packages_archive_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
