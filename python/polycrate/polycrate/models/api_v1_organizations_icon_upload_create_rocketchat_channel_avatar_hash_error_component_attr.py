from typing import Literal

ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponentAttr = Literal[
    "rocketchat_channel_avatar_hash"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponentAttr
] = {
    "rocketchat_channel_avatar_hash",
}


def check_api_v1_organizations_icon_upload_create_rocketchat_channel_avatar_hash_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
