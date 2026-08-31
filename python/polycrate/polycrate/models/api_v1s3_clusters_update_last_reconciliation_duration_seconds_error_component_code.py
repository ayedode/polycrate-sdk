from typing import Literal

ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponentCode = Literal["invalid", "max_string_length"]

API_V1S3_CLUSTERS_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
}


def check_api_v1s3_clusters_update_last_reconciliation_duration_seconds_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
