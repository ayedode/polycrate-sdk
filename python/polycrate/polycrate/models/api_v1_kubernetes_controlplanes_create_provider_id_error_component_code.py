from typing import Literal

ApiV1KubernetesControlplanesCreateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesCreateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_create_provider_id_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesCreateProviderIdErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
