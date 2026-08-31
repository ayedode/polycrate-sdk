from typing import Literal

ApiV1PolicyBindingsCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_POLICY_BINDINGS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PolicyBindingsCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_policy_bindings_create_scope_error_component_code(
    value: str,
) -> ApiV1PolicyBindingsCreateScopeErrorComponentCode:
    if value in API_V1_POLICY_BINDINGS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
