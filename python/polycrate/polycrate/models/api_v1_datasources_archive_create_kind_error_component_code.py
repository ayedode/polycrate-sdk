from typing import Literal

ApiV1DatasourcesArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DATASOURCES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_datasources_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1DatasourcesArchiveCreateKindErrorComponentCode:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
