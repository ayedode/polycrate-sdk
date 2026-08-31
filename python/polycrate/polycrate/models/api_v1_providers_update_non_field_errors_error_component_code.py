from typing import Literal

ApiV1ProvidersUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ProvidersUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_PROVIDERS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
