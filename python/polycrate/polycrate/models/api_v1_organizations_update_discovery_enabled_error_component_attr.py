from typing import Literal

ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_ORGANIZATIONS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_organizations_update_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
