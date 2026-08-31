from typing import Literal

ApiV1S3BucketsListKindItem = Literal["generic"]

API_V1S3_BUCKETS_LIST_KIND_ITEM_VALUES: set[ApiV1S3BucketsListKindItem] = {
    "generic",
}


def check_api_v1s3_buckets_list_kind_item(value: str) -> ApiV1S3BucketsListKindItem:
    if value in API_V1S3_BUCKETS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_KIND_ITEM_VALUES!r}")
