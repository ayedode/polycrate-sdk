from typing import Literal

ApiV1PoliciesPartialUpdateDescriptionErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_POLICIES_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesPartialUpdateDescriptionErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_policies_partial_update_description_error_component_code(
    value: str,
) -> ApiV1PoliciesPartialUpdateDescriptionErrorComponentCode:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
