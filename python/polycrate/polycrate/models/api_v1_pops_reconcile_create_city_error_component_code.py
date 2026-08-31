from typing import Literal

ApiV1PopsReconcileCreateCityErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_POPS_RECONCILE_CREATE_CITY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsReconcileCreateCityErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pops_reconcile_create_city_error_component_code(
    value: str,
) -> ApiV1PopsReconcileCreateCityErrorComponentCode:
    if value in API_V1_POPS_RECONCILE_CREATE_CITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_CITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
