from typing import Literal

ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_icon_upload_create_rocketchat_channel_announcement_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
