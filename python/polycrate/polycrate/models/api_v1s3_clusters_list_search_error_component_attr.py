from typing import Literal

ApiV1S3ClustersListSearchErrorComponentAttr = Literal["search"]

API_V1S3_CLUSTERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1s3_clusters_list_search_error_component_attr(value: str) -> ApiV1S3ClustersListSearchErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
