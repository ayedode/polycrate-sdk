from typing import Literal

ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_discover_create_rocketchat_channel_avatar_hash_error_component_code(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
