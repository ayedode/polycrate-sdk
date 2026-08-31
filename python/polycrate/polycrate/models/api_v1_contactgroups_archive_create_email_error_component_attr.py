from typing import Literal

ApiV1ContactgroupsArchiveCreateEmailErrorComponentAttr = Literal["email"]

API_V1_CONTACTGROUPS_ARCHIVE_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsArchiveCreateEmailErrorComponentAttr
] = {
    "email",
}


def check_api_v1_contactgroups_archive_create_email_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsArchiveCreateEmailErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_ARCHIVE_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_ARCHIVE_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
