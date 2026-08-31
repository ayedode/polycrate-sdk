from typing import Literal

ApiV1PoliciesPartialUpdateKindsSelectorErrorComponentAttr = Literal["kinds_selector"]

API_V1_POLICIES_PARTIAL_UPDATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesPartialUpdateKindsSelectorErrorComponentAttr
] = {
    "kinds_selector",
}


def check_api_v1_policies_partial_update_kinds_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesPartialUpdateKindsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
