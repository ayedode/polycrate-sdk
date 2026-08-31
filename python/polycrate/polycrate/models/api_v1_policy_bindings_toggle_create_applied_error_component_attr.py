from typing import Literal

ApiV1PolicyBindingsToggleCreateAppliedErrorComponentAttr = Literal["applied"]

API_V1_POLICY_BINDINGS_TOGGLE_CREATE_APPLIED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsToggleCreateAppliedErrorComponentAttr
] = {
    "applied",
}


def check_api_v1_policy_bindings_toggle_create_applied_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsToggleCreateAppliedErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_TOGGLE_CREATE_APPLIED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_TOGGLE_CREATE_APPLIED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
