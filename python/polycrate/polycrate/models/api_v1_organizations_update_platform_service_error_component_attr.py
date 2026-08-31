from typing import Literal

ApiV1OrganizationsUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ORGANIZATIONS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_organizations_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
