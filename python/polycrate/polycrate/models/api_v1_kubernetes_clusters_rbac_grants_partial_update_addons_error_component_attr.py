from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponentAttr = Literal["addons"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_ADDONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponentAttr
] = {
    "addons",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_addons_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_ADDONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_ADDONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
