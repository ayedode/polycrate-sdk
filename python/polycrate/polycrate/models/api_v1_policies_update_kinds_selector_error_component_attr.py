from typing import Literal

ApiV1PoliciesUpdateKindsSelectorErrorComponentAttr = Literal["kinds_selector"]

API_V1_POLICIES_UPDATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesUpdateKindsSelectorErrorComponentAttr
] = {
    "kinds_selector",
}


def check_api_v1_policies_update_kinds_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesUpdateKindsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
