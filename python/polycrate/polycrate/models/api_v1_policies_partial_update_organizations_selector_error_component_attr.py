from typing import Literal

ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponentAttr = Literal["organizations_selector"]

API_V1_POLICIES_PARTIAL_UPDATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponentAttr
] = {
    "organizations_selector",
}


def check_api_v1_policies_partial_update_organizations_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
