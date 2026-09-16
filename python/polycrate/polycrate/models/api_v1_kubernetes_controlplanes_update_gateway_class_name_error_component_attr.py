from typing import Literal

ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponentAttr = Literal["gateway_class_name"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_GATEWAY_CLASS_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponentAttr
] = {
    "gateway_class_name",
}


def check_api_v1_kubernetes_controlplanes_update_gateway_class_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_GATEWAY_CLASS_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_GATEWAY_CLASS_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
