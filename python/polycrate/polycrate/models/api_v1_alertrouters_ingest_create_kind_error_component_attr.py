from typing import Literal

ApiV1AlertroutersIngestCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ALERTROUTERS_INGEST_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_alertrouters_ingest_create_kind_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateKindErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
