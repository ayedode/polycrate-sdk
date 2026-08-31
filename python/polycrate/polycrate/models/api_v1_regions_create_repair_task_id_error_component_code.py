from typing import Literal

ApiV1RegionsCreateRepairTaskIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_REGIONS_CREATE_REPAIR_TASK_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsCreateRepairTaskIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_regions_create_repair_task_id_error_component_code(
    value: str,
) -> ApiV1RegionsCreateRepairTaskIdErrorComponentCode:
    if value in API_V1_REGIONS_CREATE_REPAIR_TASK_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_REPAIR_TASK_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
