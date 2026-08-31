from typing import Literal

ApiV1DatasourcesUpdateIsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_UPDATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesUpdateIsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_update_is_enabled_error_component_code(
    value: str,
) -> ApiV1DatasourcesUpdateIsEnabledErrorComponentCode:
    if value in API_V1_DATASOURCES_UPDATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
