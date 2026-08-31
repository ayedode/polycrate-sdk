from typing import Literal

ApiV1BackupsBackupsListS3BucketErrorComponentAttr = Literal["s3_bucket"]

API_V1_BACKUPS_BACKUPS_LIST_S3_BUCKET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsListS3BucketErrorComponentAttr
] = {
    "s3_bucket",
}


def check_api_v1_backups_backups_list_s3_bucket_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListS3BucketErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_S3_BUCKET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_S3_BUCKET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
