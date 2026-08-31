from typing import Literal

ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponentAttr = Literal["rocketchat_channel_name"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponentAttr
] = {
    "rocketchat_channel_name",
}


def check_api_v1_organizations_discover_create_rocketchat_channel_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
