from typing import Literal

ApiV1S3ClustersCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1S3_CLUSTERS_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1s3_clusters_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
