from typing import Literal

ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DATASOURCES_PARTIAL_UPDATE_LAST_SYNC_ERROR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_datasources_partial_update_last_sync_error_error_component_code(
    value: str,
) -> ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponentCode:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_LAST_SYNC_ERROR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_LAST_SYNC_ERROR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
