from typing import Literal

ApiV1AlertsCreateGeneratorUrlErrorComponentAttr = Literal["generator_url"]

API_V1_ALERTS_CREATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreateGeneratorUrlErrorComponentAttr] = {
    "generator_url",
}


def check_api_v1_alerts_create_generator_url_error_component_attr(
    value: str,
) -> ApiV1AlertsCreateGeneratorUrlErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
