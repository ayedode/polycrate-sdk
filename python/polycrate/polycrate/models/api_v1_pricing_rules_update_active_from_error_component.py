from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_v1_pricing_rules_update_active_from_error_component_attr import (
    ApiV1PricingRulesUpdateActiveFromErrorComponentAttr,
    check_api_v1_pricing_rules_update_active_from_error_component_attr,
)
from ..models.api_v1_pricing_rules_update_active_from_error_component_code import (
    ApiV1PricingRulesUpdateActiveFromErrorComponentCode,
    check_api_v1_pricing_rules_update_active_from_error_component_code,
)

T = TypeVar("T", bound="ApiV1PricingRulesUpdateActiveFromErrorComponent")


@_attrs_define
class ApiV1PricingRulesUpdateActiveFromErrorComponent:
    """
    Attributes:
        attr (ApiV1PricingRulesUpdateActiveFromErrorComponentAttr): * `active_from` - active_from
        code (ApiV1PricingRulesUpdateActiveFromErrorComponentCode): * `datetime` - datetime
            * `invalid` - invalid
        detail (str):
    """

    attr: ApiV1PricingRulesUpdateActiveFromErrorComponentAttr
    code: ApiV1PricingRulesUpdateActiveFromErrorComponentCode
    detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attr: str = self.attr

        code: str = self.code

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attr": attr,
                "code": code,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attr = check_api_v1_pricing_rules_update_active_from_error_component_attr(d.pop("attr"))

        code = check_api_v1_pricing_rules_update_active_from_error_component_code(d.pop("code"))

        detail = d.pop("detail")

        api_v1_pricing_rules_update_active_from_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        api_v1_pricing_rules_update_active_from_error_component.additional_properties = d
        return api_v1_pricing_rules_update_active_from_error_component

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
