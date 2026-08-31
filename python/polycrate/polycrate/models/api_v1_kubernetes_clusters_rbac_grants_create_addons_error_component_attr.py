from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponentAttr = Literal["addons"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_ADDONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponentAttr
] = {
    "addons",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_addons_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_ADDONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_ADDONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
