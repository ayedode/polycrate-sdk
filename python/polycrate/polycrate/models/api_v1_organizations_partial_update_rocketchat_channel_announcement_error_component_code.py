from typing import Literal

ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_partial_update_rocketchat_channel_announcement_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
