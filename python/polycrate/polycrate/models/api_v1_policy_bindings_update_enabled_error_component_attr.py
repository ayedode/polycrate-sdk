from typing import Literal

ApiV1PolicyBindingsUpdateEnabledErrorComponentAttr = Literal["enabled"]

API_V1_POLICY_BINDINGS_UPDATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsUpdateEnabledErrorComponentAttr
] = {
    "enabled",
}


def check_api_v1_policy_bindings_update_enabled_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsUpdateEnabledErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_UPDATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_UPDATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
