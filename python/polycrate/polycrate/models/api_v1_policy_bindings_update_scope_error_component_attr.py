from typing import Literal

ApiV1PolicyBindingsUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_POLICY_BINDINGS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_policy_bindings_update_scope_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsUpdateScopeErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
