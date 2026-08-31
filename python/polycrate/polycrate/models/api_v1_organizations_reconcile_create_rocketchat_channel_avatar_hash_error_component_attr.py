from typing import Literal

ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponentAttr = Literal[
    "rocketchat_channel_avatar_hash"
]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponentAttr
] = {
    "rocketchat_channel_avatar_hash",
}


def check_api_v1_organizations_reconcile_create_rocketchat_channel_avatar_hash_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_ROCKETCHAT_CHANNEL_AVATAR_HASH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
