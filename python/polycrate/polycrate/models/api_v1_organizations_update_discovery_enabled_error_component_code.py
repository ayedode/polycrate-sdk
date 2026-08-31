from typing import Literal

ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_update_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
