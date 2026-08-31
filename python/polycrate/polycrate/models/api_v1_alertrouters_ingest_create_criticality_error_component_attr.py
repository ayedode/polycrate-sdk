from typing import Literal

ApiV1AlertroutersIngestCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ALERTROUTERS_INGEST_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_alertrouters_ingest_create_criticality_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateCriticalityErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
