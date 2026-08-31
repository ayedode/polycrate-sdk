from typing import Literal

ApiV1DatasourcesArchiveCreateIsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_ARCHIVE_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesArchiveCreateIsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_archive_create_is_enabled_error_component_code(
    value: str,
) -> ApiV1DatasourcesArchiveCreateIsEnabledErrorComponentCode:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
