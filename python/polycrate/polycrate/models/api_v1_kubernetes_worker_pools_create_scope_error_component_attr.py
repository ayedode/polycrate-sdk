from typing import Literal

ApiV1KubernetesWorkerPoolsCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_worker_pools_create_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
