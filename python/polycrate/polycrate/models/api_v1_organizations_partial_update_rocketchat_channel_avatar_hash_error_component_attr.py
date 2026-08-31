from typing import Literal

ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponentAttr = Literal["rocketchat_channel_avatar_hash"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponentAttr
] = {
    "rocketchat_channel_avatar_hash",
}


def check_api_v1_organizations_partial_update_rocketchat_channel_avatar_hash_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
