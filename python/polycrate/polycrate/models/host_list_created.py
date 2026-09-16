from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_list_created_created_by_type_0 import HostListCreatedCreatedByType0


T = TypeVar("T", bound="HostListCreated")


@_attrs_define
class HostListCreated:
    """
    Attributes:
        created_at (datetime.datetime | None | Unset):
        created_at_humanized (None | str | Unset):
        created_at_display (None | str | Unset):
        created_by (HostListCreatedCreatedByType0 | None | Unset):
    """

    created_at: datetime.datetime | None | Unset = UNSET
    created_at_humanized: None | str | Unset = UNSET
    created_at_display: None | str | Unset = UNSET
    created_by: HostListCreatedCreatedByType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.host_list_created_created_by_type_0 import HostListCreatedCreatedByType0  # noqa: PLC0415

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_at_humanized: None | str | Unset
        if isinstance(self.created_at_humanized, Unset):
            created_at_humanized = UNSET
        else:
            created_at_humanized = self.created_at_humanized

        created_at_display: None | str | Unset
        if isinstance(self.created_at_display, Unset):
            created_at_display = UNSET
        else:
            created_at_display = self.created_at_display

        created_by: dict[str, Any] | None | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, HostListCreatedCreatedByType0):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_at_humanized is not UNSET:
            field_dict["created_at_humanized"] = created_at_humanized
        if created_at_display is not UNSET:
            field_dict["created_at_display"] = created_at_display
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.host_list_created_created_by_type_0 import HostListCreatedCreatedByType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_created_at_humanized(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at_humanized = _parse_created_at_humanized(d.pop("created_at_humanized", UNSET))

        def _parse_created_at_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at_display = _parse_created_at_display(d.pop("created_at_display", UNSET))

        def _parse_created_by(data: object) -> HostListCreatedCreatedByType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_type_0 = HostListCreatedCreatedByType0.from_dict(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostListCreatedCreatedByType0 | None | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        host_list_created = cls(
            created_at=created_at,
            created_at_humanized=created_at_humanized,
            created_at_display=created_at_display,
            created_by=created_by,
        )

        host_list_created.additional_properties = d
        return host_list_created

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
