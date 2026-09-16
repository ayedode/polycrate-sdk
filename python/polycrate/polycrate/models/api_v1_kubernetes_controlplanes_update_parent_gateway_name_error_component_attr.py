from typing import Literal

ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponentAttr = Literal["parent_gateway_name"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponentAttr
] = {
    "parent_gateway_name",
}


def check_api_v1_kubernetes_controlplanes_update_parent_gateway_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PARENT_GATEWAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
