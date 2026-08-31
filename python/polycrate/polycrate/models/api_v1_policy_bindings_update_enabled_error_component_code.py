from typing import Literal

ApiV1PolicyBindingsUpdateEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICY_BINDINGS_UPDATE_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsUpdateEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policy_bindings_update_enabled_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsUpdateEnabledErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_UPDATE_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_UPDATE_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
