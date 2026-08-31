from typing import Literal

ApiV1PolicyBindingsUpdateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_POLICY_BINDINGS_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsUpdateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_policy_bindings_update_scope_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsUpdateScopeErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
