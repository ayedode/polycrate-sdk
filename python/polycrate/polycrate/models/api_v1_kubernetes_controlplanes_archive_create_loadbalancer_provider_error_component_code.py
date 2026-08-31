from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_archive_create_loadbalancer_provider_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
