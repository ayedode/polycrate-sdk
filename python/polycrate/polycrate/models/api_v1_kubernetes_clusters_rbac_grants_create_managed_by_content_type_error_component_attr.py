from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
