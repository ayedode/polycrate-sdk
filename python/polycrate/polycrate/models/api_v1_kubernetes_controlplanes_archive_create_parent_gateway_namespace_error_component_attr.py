from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateParentGatewayNamespaceErrorComponentAttr = Literal["parent_gateway_namespace"]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateParentGatewayNamespaceErrorComponentAttr
] = {
    "parent_gateway_namespace",
}


def check_api_v1_kubernetes_controlplanes_archive_create_parent_gateway_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateParentGatewayNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
