from typing import Literal

ApiV1S3ClustersUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1S3_CLUSTERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1s3_clusters_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
