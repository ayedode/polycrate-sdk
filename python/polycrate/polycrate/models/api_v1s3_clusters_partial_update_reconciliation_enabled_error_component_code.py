from typing import Literal

ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_clusters_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
