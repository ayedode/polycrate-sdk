from typing import Literal

ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponentAttr = Literal[
    "rocketchat_channel_announcement"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponentAttr
] = {
    "rocketchat_channel_announcement",
}


def check_api_v1_organizations_icon_upload_create_rocketchat_channel_announcement_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
