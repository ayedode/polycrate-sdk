from typing import Literal

ApiV1ContactgroupsUpdateNameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_CONTACTGROUPS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactgroupsUpdateNameErrorComponentCode] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contactgroups_update_name_error_component_code(
    value: str,
) -> ApiV1ContactgroupsUpdateNameErrorComponentCode:
    if value in API_V1_CONTACTGROUPS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
