from typing import Literal

ApiV1BackupsBackupsListS3BucketErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_BACKUPS_BACKUPS_LIST_S3_BUCKET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsListS3BucketErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_backups_backups_list_s3_bucket_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsListS3BucketErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_LIST_S3_BUCKET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_S3_BUCKET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
