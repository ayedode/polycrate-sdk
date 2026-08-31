from typing import Literal

ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponentAttr = Literal["organizations_selector"]

API_V1_POLICIES_DRY_RUN_CREATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponentAttr
] = {
    "organizations_selector",
}


def check_api_v1_policies_dry_run_create_organizations_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateOrganizationsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_ORGANIZATIONS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
