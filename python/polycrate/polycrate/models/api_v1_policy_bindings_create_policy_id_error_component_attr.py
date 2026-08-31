from typing import Literal

ApiV1PolicyBindingsCreatePolicyIdErrorComponentAttr = Literal["policy_id"]

API_V1_POLICY_BINDINGS_CREATE_POLICY_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PolicyBindingsCreatePolicyIdErrorComponentAttr
] = {
    "policy_id",
}


def check_api_v1_policy_bindings_create_policy_id_error_component_attr(
    value: str,
) -> ApiV1PolicyBindingsCreatePolicyIdErrorComponentAttr:
    if value in API_V1_POLICY_BINDINGS_CREATE_POLICY_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICY_BINDINGS_CREATE_POLICY_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
