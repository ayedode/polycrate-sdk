from typing import Literal

ApiV1S3ClustersCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1S3_CLUSTERS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1s3_clusters_create_description_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateDescriptionErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
