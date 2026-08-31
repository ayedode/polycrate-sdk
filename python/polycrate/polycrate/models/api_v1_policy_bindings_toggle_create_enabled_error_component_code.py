from typing import Literal

ApiV1PolicyBindingsToggleCreateEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICY_BINDINGS_TOGGLE_CREATE_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsToggleCreateEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policy_bindings_toggle_create_enabled_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsToggleCreateEnabledErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_TOGGLE_CREATE_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_TOGGLE_CREATE_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
