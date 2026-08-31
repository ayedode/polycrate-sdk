from typing import Literal

ApiV1S3BucketsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1S3_BUCKETS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3BucketsListWorkspacesErrorComponentAttr] = {
    "workspaces",
}


def check_api_v1s3_buckets_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1S3BucketsListWorkspacesErrorComponentAttr:
    if value in API_V1S3_BUCKETS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
