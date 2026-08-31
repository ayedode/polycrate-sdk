from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PricingQuoteWorkspaceSimple")


@_attrs_define
class PricingQuoteWorkspaceSimple:
    """
    Attributes:
        id (UUID):
        label (str):
        total_price (None | str):
        hosts_count (int):
    """

    id: UUID
    label: str
    total_price: None | str
    hosts_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        label = self.label

        total_price: None | str
        total_price = self.total_price

        hosts_count = self.hosts_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "total_price": total_price,
                "hosts_count": hosts_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        label = d.pop("label")

        def _parse_total_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        total_price = _parse_total_price(d.pop("total_price"))

        hosts_count = d.pop("hosts_count")

        pricing_quote_workspace_simple = cls(
            id=id,
            label=label,
            total_price=total_price,
            hosts_count=hosts_count,
        )

        pricing_quote_workspace_simple.additional_properties = d
        return pricing_quote_workspace_simple

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
