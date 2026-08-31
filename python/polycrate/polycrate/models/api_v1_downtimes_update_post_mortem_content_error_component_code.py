from typing import Literal

ApiV1DowntimesUpdatePostMortemContentErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOWNTIMES_UPDATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesUpdatePostMortemContentErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_downtimes_update_post_mortem_content_error_component_code(
    value: str,
) -> ApiV1DowntimesUpdatePostMortemContentErrorComponentCode:
    if value in API_V1_DOWNTIMES_UPDATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
