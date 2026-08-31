from typing import Literal

ApiV1OrganizationsUpdateDomainsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_UPDATE_DOMAINS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateDomainsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_update_domains_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateDomainsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_DOMAINS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_DOMAINS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
