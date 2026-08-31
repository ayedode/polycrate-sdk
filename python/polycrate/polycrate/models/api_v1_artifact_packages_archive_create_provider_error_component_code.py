from typing import Literal

ApiV1ArtifactPackagesArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_artifact_packages_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateProviderErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
