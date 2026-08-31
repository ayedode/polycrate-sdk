from typing import Literal

ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_organizations_icon_upload_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
