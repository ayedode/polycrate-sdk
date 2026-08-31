from typing import Literal

ApiV1DeliveryControllersCreateK8SAppErrorComponentAttr = Literal["k8s_app"]

API_V1_DELIVERY_CONTROLLERS_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersCreateK8SAppErrorComponentAttr
] = {
    "k8s_app",
}


def check_api_v1_delivery_controllers_create_k8s_app_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersCreateK8SAppErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
