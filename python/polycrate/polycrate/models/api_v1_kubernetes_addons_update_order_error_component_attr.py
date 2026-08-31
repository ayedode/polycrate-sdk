from typing import Literal

ApiV1KubernetesAddonsUpdateOrderErrorComponentAttr = Literal["order"]

API_V1_KUBERNETES_ADDONS_UPDATE_ORDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateOrderErrorComponentAttr
] = {
    "order",
}


def check_api_v1_kubernetes_addons_update_order_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateOrderErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_ORDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_ORDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
