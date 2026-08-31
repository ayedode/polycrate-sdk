from typing import Literal

ApiV1S3ClustersUpdateDefaultProductErrorComponentAttr = Literal["default_product"]

API_V1S3_CLUSTERS_UPDATE_DEFAULT_PRODUCT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateDefaultProductErrorComponentAttr
] = {
    "default_product",
}


def check_api_v1s3_clusters_update_default_product_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateDefaultProductErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_DEFAULT_PRODUCT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_DEFAULT_PRODUCT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
