from typing import Literal

ApiV1EndpointsReconcileCreateS3ClusterErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ENDPOINTS_RECONCILE_CREATE_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsReconcileCreateS3ClusterErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_endpoints_reconcile_create_s3_cluster_error_component_code(
    value: str,
) -> ApiV1EndpointsReconcileCreateS3ClusterErrorComponentCode:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
