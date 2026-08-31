from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
