from typing import Literal

ApiV1DowntimesCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOWNTIMES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DowntimesCreateNameErrorComponentCode] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_downtimes_create_name_error_component_code(value: str) -> ApiV1DowntimesCreateNameErrorComponentCode:
    if value in API_V1_DOWNTIMES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
