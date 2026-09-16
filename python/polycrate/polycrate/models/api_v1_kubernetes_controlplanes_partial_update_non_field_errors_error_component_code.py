from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null", "unique"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
    "unique",
}


def check_api_v1_kubernetes_controlplanes_partial_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
