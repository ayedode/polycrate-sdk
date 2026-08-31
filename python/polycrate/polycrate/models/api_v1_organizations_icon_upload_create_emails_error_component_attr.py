from typing import Literal

ApiV1OrganizationsIconUploadCreateEmailsErrorComponentAttr = Literal["emails"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateEmailsErrorComponentAttr
] = {
    "emails",
}


def check_api_v1_organizations_icon_upload_create_emails_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateEmailsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
