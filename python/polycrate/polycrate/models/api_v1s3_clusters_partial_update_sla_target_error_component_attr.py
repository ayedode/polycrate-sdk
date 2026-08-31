from typing import Literal

ApiV1S3ClustersPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1s3_clusters_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
