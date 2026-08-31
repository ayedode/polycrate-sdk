from typing import Literal

ApiV1KubernetesClustersCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_create_platform_service_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersCreatePlatformServiceErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
