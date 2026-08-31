from typing import Literal

ApiV1PopsUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_POPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsUpdateTolerationsErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_pops_update_tolerations_error_component_code(
    value: str,
) -> ApiV1PopsUpdateTolerationsErrorComponentCode:
    if value in API_V1_POPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
