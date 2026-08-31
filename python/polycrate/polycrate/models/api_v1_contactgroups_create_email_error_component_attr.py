from typing import Literal

ApiV1ContactgroupsCreateEmailErrorComponentAttr = Literal["email"]

API_V1_CONTACTGROUPS_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactgroupsCreateEmailErrorComponentAttr] = {
    "email",
}


def check_api_v1_contactgroups_create_email_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsCreateEmailErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_CREATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
