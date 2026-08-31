from typing import Literal

ApiV1DatasourcesSyncCreateSlaTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_DATASOURCES_SYNC_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesSyncCreateSlaTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_datasources_sync_create_sla_target_error_component_code(
    value: str,
) -> ApiV1DatasourcesSyncCreateSlaTargetErrorComponentCode:
    if value in API_V1_DATASOURCES_SYNC_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_SLA_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
