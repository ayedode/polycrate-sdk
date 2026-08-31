from typing import Literal

ApiV1MaintenancesArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_MAINTENANCES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_maintenances_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1MaintenancesArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_MAINTENANCES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
