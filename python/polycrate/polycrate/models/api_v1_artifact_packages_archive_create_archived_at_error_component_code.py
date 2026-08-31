from typing import Literal

ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_artifact_packages_archive_create_archived_at_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
