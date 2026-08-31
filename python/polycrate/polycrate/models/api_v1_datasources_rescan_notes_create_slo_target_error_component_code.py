from typing import Literal

ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_datasources_rescan_notes_create_slo_target_error_component_code(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateSloTargetErrorComponentCode:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
