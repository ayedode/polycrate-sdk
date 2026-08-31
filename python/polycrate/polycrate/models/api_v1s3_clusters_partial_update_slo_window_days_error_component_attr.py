from typing import Literal

ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1s3_clusters_partial_update_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
