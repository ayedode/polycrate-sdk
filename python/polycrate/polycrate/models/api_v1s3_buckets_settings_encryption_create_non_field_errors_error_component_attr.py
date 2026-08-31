from typing import Literal

ApiV1S3BucketsSettingsEncryptionCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1S3_BUCKETS_SETTINGS_ENCRYPTION_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsSettingsEncryptionCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1s3_buckets_settings_encryption_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1S3BucketsSettingsEncryptionCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1S3_BUCKETS_SETTINGS_ENCRYPTION_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_SETTINGS_ENCRYPTION_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
