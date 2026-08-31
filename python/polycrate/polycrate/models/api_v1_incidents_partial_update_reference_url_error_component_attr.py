from typing import Literal

ApiV1IncidentsPartialUpdateReferenceUrlErrorComponentAttr = Literal["reference_url"]

API_V1_INCIDENTS_PARTIAL_UPDATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateReferenceUrlErrorComponentAttr
] = {
    "reference_url",
}


def check_api_v1_incidents_partial_update_reference_url_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateReferenceUrlErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
