from typing import Literal

ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDONS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addons_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
