from typing import Literal

ApiV1S3BucketsSettingsEncryptionCreateEnabledErrorComponentCode = Literal["invalid", "null", "required"]

API_V1S3_BUCKETS_SETTINGS_ENCRYPTION_CREATE_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsSettingsEncryptionCreateEnabledErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1s3_buckets_settings_encryption_create_enabled_error_component_code(
    value: str,
) -> ApiV1S3BucketsSettingsEncryptionCreateEnabledErrorComponentCode:
    if value in API_V1S3_BUCKETS_SETTINGS_ENCRYPTION_CREATE_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_SETTINGS_ENCRYPTION_CREATE_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
