from typing import Literal

ApiV1S3ClustersUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1S3_CLUSTERS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1s3_clusters_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateProviderIdErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
