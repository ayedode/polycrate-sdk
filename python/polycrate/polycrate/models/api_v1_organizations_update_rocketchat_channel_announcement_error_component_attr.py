from typing import Literal

ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponentAttr = Literal["rocketchat_channel_announcement"]

API_V1_ORGANIZATIONS_UPDATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponentAttr
] = {
    "rocketchat_channel_announcement",
}


def check_api_v1_organizations_update_rocketchat_channel_announcement_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
