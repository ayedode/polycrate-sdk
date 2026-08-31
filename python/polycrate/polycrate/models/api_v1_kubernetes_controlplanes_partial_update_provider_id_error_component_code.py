from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_partial_update_provider_id_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
