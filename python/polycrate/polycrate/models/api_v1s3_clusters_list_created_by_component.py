from typing import Literal

ApiV1S3ClustersListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1S3_CLUSTERS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1S3ClustersListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1s3_clusters_list_created_by_component(value: str) -> ApiV1S3ClustersListCreatedByComponent:
    if value in API_V1S3_CLUSTERS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
