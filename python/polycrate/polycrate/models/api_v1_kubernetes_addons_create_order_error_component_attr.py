from typing import Literal

ApiV1KubernetesAddonsCreateOrderErrorComponentAttr = Literal["order"]

API_V1_KUBERNETES_ADDONS_CREATE_ORDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsCreateOrderErrorComponentAttr
] = {
    "order",
}


def check_api_v1_kubernetes_addons_create_order_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsCreateOrderErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_ORDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_ORDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
