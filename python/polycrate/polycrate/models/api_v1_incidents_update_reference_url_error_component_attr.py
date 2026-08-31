from typing import Literal

ApiV1IncidentsUpdateReferenceUrlErrorComponentAttr = Literal["reference_url"]

API_V1_INCIDENTS_UPDATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateReferenceUrlErrorComponentAttr
] = {
    "reference_url",
}


def check_api_v1_incidents_update_reference_url_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateReferenceUrlErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_REFERENCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
