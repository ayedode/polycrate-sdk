from typing import Literal

ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_datasources_rescan_notes_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateSlaTargetErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
