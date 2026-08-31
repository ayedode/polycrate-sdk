from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponentAttr = Literal["provider_account_id"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponentAttr
] = {
    "provider_account_id",
}


def check_api_v1_kubernetes_worker_pools_update_provider_account_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateProviderAccountIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
