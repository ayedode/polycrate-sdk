from typing import Literal

ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponentAttr = Literal["provider_account"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_PROVIDER_ACCOUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponentAttr
] = {
    "provider_account",
}


def check_api_v1_kubernetes_worker_pools_list_provider_account_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListProviderAccountErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_PROVIDER_ACCOUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_PROVIDER_ACCOUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
