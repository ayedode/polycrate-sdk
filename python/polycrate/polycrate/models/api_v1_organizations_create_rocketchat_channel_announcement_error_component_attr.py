from typing import Literal

ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponentAttr = Literal["rocketchat_channel_announcement"]

API_V1_ORGANIZATIONS_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponentAttr
] = {
    "rocketchat_channel_announcement",
}


def check_api_v1_organizations_create_rocketchat_channel_announcement_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
