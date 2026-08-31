from typing import Literal

ApiV1ContactgroupsCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONTACTGROUPS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactgroupsCreateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_contactgroups_create_kind_error_component_code(
    value: str,
) -> ApiV1ContactgroupsCreateKindErrorComponentCode:
    if value in API_V1_CONTACTGROUPS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
