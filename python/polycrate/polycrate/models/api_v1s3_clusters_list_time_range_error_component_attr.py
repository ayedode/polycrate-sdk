from typing import Literal

ApiV1S3ClustersListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1S3_CLUSTERS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersListTimeRangeErrorComponentAttr] = {
    "time_range",
}


def check_api_v1s3_clusters_list_time_range_error_component_attr(
    value: str,
) -> ApiV1S3ClustersListTimeRangeErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
