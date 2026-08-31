from typing import Literal

ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponentAttr = Literal["rocketchat_channel_id"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponentAttr
] = {
    "rocketchat_channel_id",
}


def check_api_v1_organizations_icon_upload_create_rocketchat_channel_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
