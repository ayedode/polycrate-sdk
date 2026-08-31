from typing import Literal

ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponentAttr = Literal["rocketchat_channel_name"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponentAttr
] = {
    "rocketchat_channel_name",
}


def check_api_v1_organizations_icon_upload_create_rocketchat_channel_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ROCKETCHAT_CHANNEL_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
