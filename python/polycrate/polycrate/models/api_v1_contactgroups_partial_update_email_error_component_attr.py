from typing import Literal

ApiV1ContactgroupsPartialUpdateEmailErrorComponentAttr = Literal["email"]

API_V1_CONTACTGROUPS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsPartialUpdateEmailErrorComponentAttr
] = {
    "email",
}


def check_api_v1_contactgroups_partial_update_email_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsPartialUpdateEmailErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_PARTIAL_UPDATE_EMAIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
