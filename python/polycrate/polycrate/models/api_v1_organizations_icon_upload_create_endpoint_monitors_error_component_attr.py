from typing import Literal

ApiV1OrganizationsIconUploadCreateEndpointMonitorsErrorComponentAttr = Literal["endpoint_monitors"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateEndpointMonitorsErrorComponentAttr
] = {
    "endpoint_monitors",
}


def check_api_v1_organizations_icon_upload_create_endpoint_monitors_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateEndpointMonitorsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
