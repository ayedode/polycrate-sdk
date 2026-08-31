from typing import Literal

ApiV1PolicyBindingsCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_POLICY_BINDINGS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_policy_bindings_create_scope_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsCreateScopeErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
