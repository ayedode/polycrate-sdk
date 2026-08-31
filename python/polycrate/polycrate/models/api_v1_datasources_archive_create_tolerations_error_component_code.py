from typing import Literal

ApiV1DatasourcesArchiveCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesArchiveCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_archive_create_tolerations_error_component_code(
    value: str,
) -> ApiV1DatasourcesArchiveCreateTolerationsErrorComponentCode:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
