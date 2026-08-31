from typing import Literal

ApiV1S3BucketsListStateNotErrorComponentAttr = Literal["state_not"]

API_V1S3_BUCKETS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3BucketsListStateNotErrorComponentAttr] = {
    "state_not",
}


def check_api_v1s3_buckets_list_state_not_error_component_attr(
    value: str,
) -> ApiV1S3BucketsListStateNotErrorComponentAttr:
    if value in API_V1S3_BUCKETS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
