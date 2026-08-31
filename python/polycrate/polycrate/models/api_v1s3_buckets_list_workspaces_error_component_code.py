from typing import Literal

ApiV1S3BucketsListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1S3_BUCKETS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3BucketsListWorkspacesErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1s3_buckets_list_workspaces_error_component_code(
    value: str,
) -> ApiV1S3BucketsListWorkspacesErrorComponentCode:
    if value in API_V1S3_BUCKETS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
