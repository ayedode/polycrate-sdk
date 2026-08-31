from typing import Literal

ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponentAttr = Literal[
    "rocketchat_channel_announcement"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponentAttr
] = {
    "rocketchat_channel_announcement",
}


def check_api_v1_organizations_discover_create_rocketchat_channel_announcement_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
