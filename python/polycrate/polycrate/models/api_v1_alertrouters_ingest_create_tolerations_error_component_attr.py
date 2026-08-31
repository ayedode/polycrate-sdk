from typing import Literal

ApiV1AlertroutersIngestCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ALERTROUTERS_INGEST_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_alertrouters_ingest_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateTolerationsErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
