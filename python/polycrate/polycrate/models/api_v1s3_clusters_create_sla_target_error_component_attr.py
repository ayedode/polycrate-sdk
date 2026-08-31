from typing import Literal

ApiV1S3ClustersCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1S3_CLUSTERS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1s3_clusters_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateSlaTargetErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
