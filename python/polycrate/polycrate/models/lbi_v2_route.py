from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lbi_v2_route_filters_item import LbiV2RouteFiltersItem
    from ..models.lbi_v2_route_match import LbiV2RouteMatch


T = TypeVar("T", bound="LbiV2Route")


@_attrs_define
class LbiV2Route:
    """
    Attributes:
        listener (str):
        backend (str):
        name (str | Unset):
        match (LbiV2RouteMatch | Unset):
        filters (list[LbiV2RouteFiltersItem] | Unset):
    """

    listener: str
    backend: str
    name: str | Unset = UNSET
    match: LbiV2RouteMatch | Unset = UNSET
    filters: list[LbiV2RouteFiltersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        listener = self.listener

        backend = self.backend

        name = self.name

        match: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listener": listener,
                "backend": backend,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if match is not UNSET:
            field_dict["match"] = match
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lbi_v2_route_filters_item import LbiV2RouteFiltersItem  # noqa: PLC0415
        from ..models.lbi_v2_route_match import LbiV2RouteMatch  # noqa: PLC0415

        d = dict(src_dict)
        listener = d.pop("listener")

        backend = d.pop("backend")

        name = d.pop("name", UNSET)

        _match = d.pop("match", UNSET)
        match: LbiV2RouteMatch | Unset
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = LbiV2RouteMatch.from_dict(_match)

        _filters = d.pop("filters", UNSET)
        filters: list[LbiV2RouteFiltersItem] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = LbiV2RouteFiltersItem.from_dict(filters_item_data)

                filters.append(filters_item)

        lbi_v2_route = cls(
            listener=listener,
            backend=backend,
            name=name,
            match=match,
            filters=filters,
        )

        lbi_v2_route.additional_properties = d
        return lbi_v2_route

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
