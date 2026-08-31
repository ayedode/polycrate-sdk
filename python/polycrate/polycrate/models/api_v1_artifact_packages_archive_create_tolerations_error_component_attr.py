from typing import Literal

ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_artifact_packages_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
