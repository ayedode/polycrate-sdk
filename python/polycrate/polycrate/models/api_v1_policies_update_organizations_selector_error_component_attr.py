from typing import Literal

ApiV1PoliciesUpdateOrganizationsSelectorErrorComponentAttr = Literal["organizations_selector"]

API_V1_POLICIES_UPDATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesUpdateOrganizationsSelectorErrorComponentAttr
] = {
    "organizations_selector",
}


def check_api_v1_policies_update_organizations_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesUpdateOrganizationsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
