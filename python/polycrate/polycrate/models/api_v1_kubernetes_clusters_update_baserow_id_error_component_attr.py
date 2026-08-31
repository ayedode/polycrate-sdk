from typing import Literal

ApiV1KubernetesClustersUpdateBaserowIdErrorComponentAttr = Literal["baserow_id"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_BASEROW_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersUpdateBaserowIdErrorComponentAttr
] = {
    "baserow_id",
}


def check_api_v1_kubernetes_clusters_update_baserow_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersUpdateBaserowIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_BASEROW_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_BASEROW_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
