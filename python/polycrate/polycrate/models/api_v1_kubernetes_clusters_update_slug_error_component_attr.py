from typing import Literal

ApiV1KubernetesClustersUpdateSlugErrorComponentAttr = Literal["slug"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersUpdateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_kubernetes_clusters_update_slug_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersUpdateSlugErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
