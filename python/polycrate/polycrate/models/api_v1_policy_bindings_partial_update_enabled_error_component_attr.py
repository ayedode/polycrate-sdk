from typing import Literal

ApiV1PolicyBindingsPartialUpdateEnabledErrorComponentAttr = Literal["enabled"]

API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsPartialUpdateEnabledErrorComponentAttr
] = {
    "enabled",
}


def check_api_v1_policy_bindings_partial_update_enabled_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsPartialUpdateEnabledErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
