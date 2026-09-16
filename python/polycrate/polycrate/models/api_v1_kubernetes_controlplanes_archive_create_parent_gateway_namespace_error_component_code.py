from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateParentGatewayNamespaceErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateParentGatewayNamespaceErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_archive_create_parent_gateway_namespace_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateParentGatewayNamespaceErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_PARENT_GATEWAY_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
