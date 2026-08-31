from typing import Literal

ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponentAttr = Literal[
    "rocketchat_channel_announcement"
]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponentAttr
] = {
    "rocketchat_channel_announcement",
}


def check_api_v1_organizations_reconcile_create_rocketchat_channel_announcement_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_ROCKETCHAT_CHANNEL_ANNOUNCEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
