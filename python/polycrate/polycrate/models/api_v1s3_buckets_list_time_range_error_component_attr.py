from typing import Literal

ApiV1S3BucketsListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1S3_BUCKETS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3BucketsListTimeRangeErrorComponentAttr] = {
    "time_range",
}


def check_api_v1s3_buckets_list_time_range_error_component_attr(
    value: str,
) -> ApiV1S3BucketsListTimeRangeErrorComponentAttr:
    if value in API_V1S3_BUCKETS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
