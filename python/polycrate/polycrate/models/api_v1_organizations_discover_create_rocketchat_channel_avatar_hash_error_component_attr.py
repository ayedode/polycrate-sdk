from typing import Literal

ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponentAttr = Literal[
    "rocketchat_channel_avatar_hash"
]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponentAttr
] = {
    "rocketchat_channel_avatar_hash",
}


def check_api_v1_organizations_discover_create_rocketchat_channel_avatar_hash_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
