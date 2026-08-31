from typing import Literal

ApiV1S3BucketsSettingsEncryptionCreateEnabledErrorComponentAttr = Literal["enabled"]

API_V1S3_BUCKETS_SETTINGS_ENCRYPTION_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsSettingsEncryptionCreateEnabledErrorComponentAttr
] = {
    "enabled",
}


def check_api_v1s3_buckets_settings_encryption_create_enabled_error_component_attr(
    value: str,
) -> ApiV1S3BucketsSettingsEncryptionCreateEnabledErrorComponentAttr:
    if value in API_V1S3_BUCKETS_SETTINGS_ENCRYPTION_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_SETTINGS_ENCRYPTION_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
