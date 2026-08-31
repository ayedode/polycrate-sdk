from typing import Literal

ApiV1PolicyBindingsToggleCreateEnabledErrorComponentAttr = Literal["enabled"]

API_V1_POLICY_BINDINGS_TOGGLE_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsToggleCreateEnabledErrorComponentAttr
] = {
    "enabled",
}


def check_api_v1_policy_bindings_toggle_create_enabled_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsToggleCreateEnabledErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_TOGGLE_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_TOGGLE_CREATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
