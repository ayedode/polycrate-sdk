from typing import Literal

ApiV1PoliciesUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_update_tolerations_error_component_code(
    value: str,
) -> ApiV1PoliciesUpdateTolerationsErrorComponentCode:
    if value in API_V1_POLICIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
