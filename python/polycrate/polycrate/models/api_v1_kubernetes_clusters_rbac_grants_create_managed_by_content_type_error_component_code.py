from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type"
]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_managed_by_content_type_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
