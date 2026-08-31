from typing import Literal

ApiV1ConditionsCreateDescriptionErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONDITIONS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionsCreateDescriptionErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_conditions_create_description_error_component_code(
    value: str,
) -> ApiV1ConditionsCreateDescriptionErrorComponentCode:
    if value in API_V1_CONDITIONS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
