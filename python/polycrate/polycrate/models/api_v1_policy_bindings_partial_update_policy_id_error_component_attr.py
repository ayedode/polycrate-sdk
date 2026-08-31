from typing import Literal

ApiV1PolicyBindingsPartialUpdatePolicyIdErrorComponentAttr = Literal["policy_id"]

API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_POLICY_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsPartialUpdatePolicyIdErrorComponentAttr
] = {
    "policy_id",
}


def check_api_v1_policy_bindings_partial_update_policy_id_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsPartialUpdatePolicyIdErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_POLICY_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_PARTIAL_UPDATE_POLICY_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
