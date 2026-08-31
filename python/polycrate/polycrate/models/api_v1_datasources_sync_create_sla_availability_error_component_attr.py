from typing import Literal

ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_DATASOURCES_SYNC_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_datasources_sync_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
