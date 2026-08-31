from typing import Literal

ApiV1KubernetesClustersPartialUpdateSlugErrorComponentAttr = Literal["slug"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_kubernetes_clusters_partial_update_slug_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateSlugErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
