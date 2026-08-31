from typing import Literal

ApiV1KubernetesClustersCreateAddonsErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_CREATE_ADDONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersCreateAddonsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_create_addons_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersCreateAddonsErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_ADDONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_ADDONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
