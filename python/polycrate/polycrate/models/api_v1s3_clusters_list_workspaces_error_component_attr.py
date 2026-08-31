from typing import Literal

ApiV1S3ClustersListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1S3_CLUSTERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersListWorkspacesErrorComponentAttr] = {
    "workspaces",
}


def check_api_v1s3_clusters_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1S3ClustersListWorkspacesErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
