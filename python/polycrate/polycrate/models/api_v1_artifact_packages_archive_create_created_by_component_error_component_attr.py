from typing import Literal

ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_artifact_packages_archive_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
