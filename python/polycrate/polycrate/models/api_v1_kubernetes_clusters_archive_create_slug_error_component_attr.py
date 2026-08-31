from typing import Literal

ApiV1KubernetesClustersArchiveCreateSlugErrorComponentAttr = Literal["slug"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_kubernetes_clusters_archive_create_slug_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateSlugErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
