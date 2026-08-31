from typing import Literal

ApiV1PolicyBindingsPartialUpdateAppliedErrorComponentAttr = Literal["applied"]

API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_APPLIED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsPartialUpdateAppliedErrorComponentAttr
] = {
    "applied",
}


def check_api_v1_policy_bindings_partial_update_applied_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsPartialUpdateAppliedErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_APPLIED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_APPLIED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
