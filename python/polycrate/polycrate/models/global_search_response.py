from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_search_response_facets import GlobalSearchResponseFacets
    from ..models.global_search_response_hits_item import GlobalSearchResponseHitsItem


T = TypeVar("T", bound="GlobalSearchResponse")


@_attrs_define
class GlobalSearchResponse:
    """
    Attributes:
        hits (list[GlobalSearchResponseHitsItem]):
        total (int):
        facets (GlobalSearchResponseFacets | Unset):
    """

    hits: list[GlobalSearchResponseHitsItem]
    total: int
    facets: GlobalSearchResponseFacets | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hits = []
        for hits_item_data in self.hits:
            hits_item = hits_item_data.to_dict()
            hits.append(hits_item)

        total = self.total

        facets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.facets, Unset):
            facets = self.facets.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hits": hits,
                "total": total,
            }
        )
        if facets is not UNSET:
            field_dict["facets"] = facets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_search_response_facets import GlobalSearchResponseFacets
        from ..models.global_search_response_hits_item import GlobalSearchResponseHitsItem

        d = dict(src_dict)
        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:
            hits_item = GlobalSearchResponseHitsItem.from_dict(hits_item_data)

            hits.append(hits_item)

        total = d.pop("total")

        _facets = d.pop("facets", UNSET)
        facets: GlobalSearchResponseFacets | Unset
        if isinstance(_facets, Unset):
            facets = UNSET
        else:
            facets = GlobalSearchResponseFacets.from_dict(_facets)

        global_search_response = cls(
            hits=hits,
            total=total,
            facets=facets,
        )

        global_search_response.additional_properties = d
        return global_search_response

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
