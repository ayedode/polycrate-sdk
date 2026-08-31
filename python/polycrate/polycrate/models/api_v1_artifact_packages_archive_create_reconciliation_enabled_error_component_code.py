from typing import Literal

ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_packages_archive_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
