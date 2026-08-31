from typing import Literal

ApiV1OrganizationsIconUploadCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_organizations_icon_upload_create_labels_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateLabelsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
