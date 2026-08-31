from typing import Literal

ApiV1PolicyBindingsPartialUpdateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsPartialUpdateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_policy_bindings_partial_update_scope_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsPartialUpdateScopeErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
