from typing import Literal

ApiV1KubernetesClustersCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_create_active_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersCreateActiveErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
