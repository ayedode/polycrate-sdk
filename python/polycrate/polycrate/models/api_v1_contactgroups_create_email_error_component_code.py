from typing import Literal

ApiV1ContactgroupsCreateEmailErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_CONTACTGROUPS_CREATE_EMAIL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactgroupsCreateEmailErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contactgroups_create_email_error_component_code(
    value: str,
) -> ApiV1ContactgroupsCreateEmailErrorComponentCode:
    if value in API_V1_CONTACTGROUPS_CREATE_EMAIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_CREATE_EMAIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
