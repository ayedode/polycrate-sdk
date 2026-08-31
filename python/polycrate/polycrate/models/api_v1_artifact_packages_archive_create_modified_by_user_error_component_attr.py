from typing import Literal

ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_artifact_packages_archive_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
