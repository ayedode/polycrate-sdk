from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponentAttr = Literal["product_id"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponentAttr
] = {
    "product_id",
}


def check_api_v1_kubernetes_worker_pools_partial_update_product_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
