from typing import Literal

ApiV1ContactgroupsUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONTACTGROUPS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactgroupsUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_contactgroups_update_kind_error_component_code(
    value: str,
) -> ApiV1ContactgroupsUpdateKindErrorComponentCode:
    if value in API_V1_CONTACTGROUPS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
