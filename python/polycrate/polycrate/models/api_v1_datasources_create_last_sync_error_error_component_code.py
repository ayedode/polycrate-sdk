from typing import Literal

ApiV1DatasourcesCreateLastSyncErrorErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DATASOURCES_CREATE_LAST_SYNC_ERROR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesCreateLastSyncErrorErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_datasources_create_last_sync_error_error_component_code(
    value: str,
) -> ApiV1DatasourcesCreateLastSyncErrorErrorComponentCode:
    if value in API_V1_DATASOURCES_CREATE_LAST_SYNC_ERROR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_LAST_SYNC_ERROR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
