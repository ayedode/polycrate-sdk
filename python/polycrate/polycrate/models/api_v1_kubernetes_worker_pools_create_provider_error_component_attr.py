from typing import Literal

ApiV1KubernetesWorkerPoolsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_kubernetes_worker_pools_create_provider_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateProviderErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
