from typing import Literal

ApiV1PolicyBindingsToggleCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_POLICY_BINDINGS_TOGGLE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsToggleCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_policy_bindings_toggle_create_scope_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsToggleCreateScopeErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_TOGGLE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_TOGGLE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
