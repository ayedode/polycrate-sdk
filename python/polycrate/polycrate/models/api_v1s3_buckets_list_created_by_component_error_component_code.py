from typing import Literal

ApiV1S3BucketsListCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1S3_BUCKETS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsListCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1s3_buckets_list_created_by_component_error_component_code(
    value: str,
) -> ApiV1S3BucketsListCreatedByComponentErrorComponentCode:
    if value in API_V1S3_BUCKETS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
