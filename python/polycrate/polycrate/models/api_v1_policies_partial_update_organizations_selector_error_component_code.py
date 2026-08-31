from typing import Literal

ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_PARTIAL_UPDATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_partial_update_organizations_selector_error_component_code(
    value: str,
) -> ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponentCode:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
