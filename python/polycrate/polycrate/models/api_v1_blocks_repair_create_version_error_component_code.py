from typing import Literal

ApiV1BlocksRepairCreateVersionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_REPAIR_CREATE_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRepairCreateVersionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_repair_create_version_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateVersionErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
