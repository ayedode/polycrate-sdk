from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_worker_pools_update_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
