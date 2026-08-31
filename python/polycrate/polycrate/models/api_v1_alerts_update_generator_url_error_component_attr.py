from typing import Literal

ApiV1AlertsUpdateGeneratorUrlErrorComponentAttr = Literal["generator_url"]

API_V1_ALERTS_UPDATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateGeneratorUrlErrorComponentAttr] = {
    "generator_url",
}


def check_api_v1_alerts_update_generator_url_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdateGeneratorUrlErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_GENERATOR_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
