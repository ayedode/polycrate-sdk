from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.last_state_enum import LastStateEnum, check_last_state_enum

T = TypeVar("T", bound="PricingQuoteSimple")


@_attrs_define
class PricingQuoteSimple:
    """
    Attributes:
        id (UUID):
        name (str):
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        total_price (None | str):
        valid_until (datetime.date | None):
    """

    id: UUID
    name: str
    state: LastStateEnum
    total_price: None | str
    valid_until: datetime.date | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        state: str = self.state

        total_price: None | str
        total_price = self.total_price

        valid_until: None | str
        if isinstance(self.valid_until, datetime.date):
            valid_until = self.valid_until.isoformat()
        else:
            valid_until = self.valid_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "total_price": total_price,
                "valid_until": valid_until,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        def _parse_total_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        total_price = _parse_total_price(d.pop("total_price"))

        def _parse_valid_until(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_until_type_0 = datetime.date.fromisoformat(data)

                return valid_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        valid_until = _parse_valid_until(d.pop("valid_until"))

        pricing_quote_simple = cls(
            id=id,
            name=name,
            state=state,
            total_price=total_price,
            valid_until=valid_until,
        )

        pricing_quote_simple.additional_properties = d
        return pricing_quote_simple

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
