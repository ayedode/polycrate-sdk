from typing import Literal

ApiV1S3ClustersCreateKindErrorComponentAttr = Literal["kind"]

API_V1S3_CLUSTERS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1s3_clusters_create_kind_error_component_attr(value: str) -> ApiV1S3ClustersCreateKindErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
