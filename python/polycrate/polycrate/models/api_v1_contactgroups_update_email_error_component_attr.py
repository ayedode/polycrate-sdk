from typing import Literal

ApiV1ContactgroupsUpdateEmailErrorComponentAttr = Literal["email"]

API_V1_CONTACTGROUPS_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactgroupsUpdateEmailErrorComponentAttr] = {
    "email",
}


def check_api_v1_contactgroups_update_email_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsUpdateEmailErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
