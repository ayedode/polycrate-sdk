from typing import Literal

ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponentAttr = Literal[
    "last_reconciliation_duration_seconds"
]

API_V1S3_CLUSTERS_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponentAttr
] = {
    "last_reconciliation_duration_seconds",
}


def check_api_v1s3_clusters_update_last_reconciliation_duration_seconds_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
