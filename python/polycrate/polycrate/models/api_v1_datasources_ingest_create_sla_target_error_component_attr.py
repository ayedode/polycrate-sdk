from typing import Literal

ApiV1DatasourcesIngestCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_DATASOURCES_INGEST_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_datasources_ingest_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateSlaTargetErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
