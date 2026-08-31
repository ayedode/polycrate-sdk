from typing import Literal

ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifacts_archive_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1ArtifactsArchiveCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
