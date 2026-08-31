from typing import Literal

ApiV1S3ClustersListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1S3_CLUSTERS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3ClustersListWorkspacesErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1s3_clusters_list_workspaces_error_component_code(
    value: str,
) -> ApiV1S3ClustersListWorkspacesErrorComponentCode:
    if value in API_V1S3_CLUSTERS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
