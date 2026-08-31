from typing import Literal

ApiV1S3ClustersCreateSlugErrorComponentAttr = Literal["slug"]

API_V1S3_CLUSTERS_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersCreateSlugErrorComponentAttr] = {
    "slug",
}


def check_api_v1s3_clusters_create_slug_error_component_attr(value: str) -> ApiV1S3ClustersCreateSlugErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
