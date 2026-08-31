from typing import Literal

ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponentAttr = Literal["product_id"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponentAttr
] = {
    "product_id",
}


def check_api_v1_kubernetes_worker_pools_create_product_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
