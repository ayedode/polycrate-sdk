from typing import Literal

ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_artifact_packages_archive_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
