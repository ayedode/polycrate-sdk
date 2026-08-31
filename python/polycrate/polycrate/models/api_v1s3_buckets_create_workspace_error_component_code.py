from typing import Literal

ApiV1S3BucketsCreateWorkspaceErrorComponentCode = Literal["does_not_exist", "incorrect_type", "required"]

API_V1S3_BUCKETS_CREATE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3BucketsCreateWorkspaceErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1s3_buckets_create_workspace_error_component_code(
    value: str,
) -> ApiV1S3BucketsCreateWorkspaceErrorComponentCode:
    if value in API_V1S3_BUCKETS_CREATE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_CREATE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
