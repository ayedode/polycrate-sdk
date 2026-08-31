from typing import Literal

ApiV1S3ClustersListNameErrorComponentAttr = Literal["name"]

API_V1S3_CLUSTERS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1s3_clusters_list_name_error_component_attr(value: str) -> ApiV1S3ClustersListNameErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
