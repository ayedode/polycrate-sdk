from typing import Literal

ApiV1PoliciesCreateOrganizationsSelectorErrorComponentAttr = Literal["organizations_selector"]

API_V1_POLICIES_CREATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesCreateOrganizationsSelectorErrorComponentAttr
] = {
    "organizations_selector",
}


def check_api_v1_policies_create_organizations_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesCreateOrganizationsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_CREATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
