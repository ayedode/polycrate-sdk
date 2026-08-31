from typing import Literal

ApiV1S3ClustersListNameExactErrorComponentAttr = Literal["name_exact"]

API_V1S3_CLUSTERS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersListNameExactErrorComponentAttr] = {
    "name_exact",
}


def check_api_v1s3_clusters_list_name_exact_error_component_attr(
    value: str,
) -> ApiV1S3ClustersListNameExactErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
