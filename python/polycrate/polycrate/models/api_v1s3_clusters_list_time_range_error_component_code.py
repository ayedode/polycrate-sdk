from typing import Literal

ApiV1S3ClustersListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1S3_CLUSTERS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3ClustersListTimeRangeErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1s3_clusters_list_time_range_error_component_code(
    value: str,
) -> ApiV1S3ClustersListTimeRangeErrorComponentCode:
    if value in API_V1S3_CLUSTERS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
