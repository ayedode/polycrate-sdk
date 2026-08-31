from typing import Literal

ApiV1OrganizationsCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_ORGANIZATIONS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_organizations_create_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
