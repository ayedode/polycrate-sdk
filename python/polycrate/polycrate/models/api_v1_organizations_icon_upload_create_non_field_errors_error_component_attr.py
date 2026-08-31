from typing import Literal

ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_organizations_icon_upload_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
