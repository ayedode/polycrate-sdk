from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationProductListRequest")


@_attrs_define
class OrganizationProductListRequest:
    """List serializer for V2 table views.

    Attributes:
        agreed_price (str):
        active_from (datetime.date | None | Unset):
        active_until (datetime.date | None | Unset):
        auto_managed (bool | Unset):
    """

    agreed_price: str
    active_from: datetime.date | None | Unset = UNSET
    active_until: datetime.date | None | Unset = UNSET
    auto_managed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agreed_price = self.agreed_price

        active_from: None | str | Unset
        if isinstance(self.active_from, Unset):
            active_from = UNSET
        elif isinstance(self.active_from, datetime.date):
            active_from = self.active_from.isoformat()
        else:
            active_from = self.active_from

        active_until: None | str | Unset
        if isinstance(self.active_until, Unset):
            active_until = UNSET
        elif isinstance(self.active_until, datetime.date):
            active_until = self.active_until.isoformat()
        else:
            active_until = self.active_until

        auto_managed = self.auto_managed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agreed_price": agreed_price,
            }
        )
        if active_from is not UNSET:
            field_dict["active_from"] = active_from
        if active_until is not UNSET:
            field_dict["active_until"] = active_until
        if auto_managed is not UNSET:
            field_dict["auto_managed"] = auto_managed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agreed_price = d.pop("agreed_price")

        def _parse_active_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_from_type_0 = datetime.date.fromisoformat(data)

                return active_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        active_from = _parse_active_from(d.pop("active_from", UNSET))

        def _parse_active_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_until_type_0 = datetime.date.fromisoformat(data)

                return active_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        active_until = _parse_active_until(d.pop("active_until", UNSET))

        auto_managed = d.pop("auto_managed", UNSET)

        organization_product_list_request = cls(
            agreed_price=agreed_price,
            active_from=active_from,
            active_until=active_until,
            auto_managed=auto_managed,
        )

        organization_product_list_request.additional_properties = d
        return organization_product_list_request

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
