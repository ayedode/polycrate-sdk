from typing import Literal

ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_buckets_archive_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1S3BucketsArchiveCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
