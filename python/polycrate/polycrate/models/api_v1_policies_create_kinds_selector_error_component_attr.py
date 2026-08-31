from typing import Literal

ApiV1PoliciesCreateKindsSelectorErrorComponentAttr = Literal["kinds_selector"]

API_V1_POLICIES_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesCreateKindsSelectorErrorComponentAttr
] = {
    "kinds_selector",
}


def check_api_v1_policies_create_kinds_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesCreateKindsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
