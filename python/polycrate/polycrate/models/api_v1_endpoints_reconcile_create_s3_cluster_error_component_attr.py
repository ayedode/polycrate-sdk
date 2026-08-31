from typing import Literal

ApiV1EndpointsReconcileCreateS3ClusterErrorComponentAttr = Literal["s3_cluster"]

API_V1_ENDPOINTS_RECONCILE_CREATE_S3_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateS3ClusterErrorComponentAttr
] = {
    "s3_cluster",
}


def check_api_v1_endpoints_reconcile_create_s3_cluster_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateS3ClusterErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_S3_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_S3_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
