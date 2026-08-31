from typing import Literal

ApiV1ProvidersCreateSlaTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PROVIDERS_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersCreateSlaTargetErrorComponentCode] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_providers_create_sla_target_error_component_code(
    value: str,
) -> ApiV1ProvidersCreateSlaTargetErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
