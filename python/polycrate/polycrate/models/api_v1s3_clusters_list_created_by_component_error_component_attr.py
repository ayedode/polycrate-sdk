from typing import Literal

ApiV1S3ClustersListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1S3_CLUSTERS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1s3_clusters_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1S3ClustersListCreatedByComponentErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
