from typing import Literal

ApiV1S3BucketsUpdateWorkspaceErrorComponentAttr = Literal["workspace"]

API_V1S3_BUCKETS_UPDATE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3BucketsUpdateWorkspaceErrorComponentAttr] = {
    "workspace",
}


def check_api_v1s3_buckets_update_workspace_error_component_attr(
    value: str,
) -> ApiV1S3BucketsUpdateWorkspaceErrorComponentAttr:
    if value in API_V1S3_BUCKETS_UPDATE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_UPDATE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
