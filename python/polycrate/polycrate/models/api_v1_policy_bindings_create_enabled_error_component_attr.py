from typing import Literal

ApiV1PolicyBindingsCreateEnabledErrorComponentAttr = Literal["enabled"]

API_V1_POLICY_BINDINGS_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsCreateEnabledErrorComponentAttr
] = {
    "enabled",
}


def check_api_v1_policy_bindings_create_enabled_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsCreateEnabledErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
