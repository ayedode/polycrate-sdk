from typing import Literal

ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_artifact_packages_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
