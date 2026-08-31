from typing import Literal

ApiV1S3BucketsSettingsVersioningCreateStatusErrorComponentAttr = Literal["status"]

API_V1S3_BUCKETS_SETTINGS_VERSIONING_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsSettingsVersioningCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1s3_buckets_settings_versioning_create_status_error_component_attr(
    value: str,
) -> ApiV1S3BucketsSettingsVersioningCreateStatusErrorComponentAttr:
    if value in API_V1S3_BUCKETS_SETTINGS_VERSIONING_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_SETTINGS_VERSIONING_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
