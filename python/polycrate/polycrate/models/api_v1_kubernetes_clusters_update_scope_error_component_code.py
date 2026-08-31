from typing import Literal

ApiV1KubernetesClustersUpdateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersUpdateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_clusters_update_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersUpdateScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
